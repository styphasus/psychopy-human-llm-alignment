from asyncio import streams
import time
from pylsl import StreamInlet, resolve_streams
import keyboard
import threading
import queue

def file_writer(filename, write_queue, stop_event):
    with open(filename, 'w') as f:
        # Write header once
        f.write("Time,TimeLsl,Fp1,Fz,F3,F7,F9,FC5,FC1,C3,T7,CP5,CP1,Pz,P3,P7,P9,O1,Oz,O2,P10,P8,P4,CP2,CP6,T8,C4,Cz,FC2,FC6,F10,F8,F4,Fp2,AF7,AF3,AFz,F1,F5,FT7,FC3,C1,C5,TP7,CP3,P1,P5,PO7,PO3,Iz,POz,PO4,PO8,P6,P2,CPz,CP4,TP8,C6,C2,FC4,FT8,F6,F2,AF4,AF8,ACC_X,ACC_Z,ACC_Y\n")
        
        while not stop_event.is_set() or not write_queue.empty():
            try:
                # Get data from queue
                data = write_queue.get(timeout=1)
                if data:
                    f.write(data)
                write_queue.task_done()
            except queue.Empty:
                continue

def main():
    print("looking for an EEG stream...")
    streams = resolve_streams()
    eeg_streams = [s for s in streams if s.type() == 'EEG']

    if not eeg_streams:
        print("No EEG stream found.")
        return

    info = eeg_streams[0]
    inlet = StreamInlet(info)
    
    timestamp = int(time.time())
    filename = f'C:\\Users\\Display\\psychopy-human-llm-alignment\\EEG\\EEG_data_{timestamp}.csv'
    # Queue to hold data before writing to file
    write_queue = queue.Queue()
    stop_event = threading.Event()
    
    # Start file writer thread
    writer_thread = threading.Thread(target=file_writer, args=(filename, write_queue, stop_event))
    writer_thread.start()

    buffer = []
    buffer_size = 6000
    
    try:
        print(f"Connected to outlet {info.name()} @ {info.hostname()}, chanCount: {inlet.channel_count}")
        while True:
            try:
                unixTime = time.time()
                offset = inlet.time_correction()

                chunk, timestamps = inlet.pull_chunk(timeout=0.01, max_samples=2048)
                
                if len(timestamps) > 0:
                    print(f"Offset: {offset} Chunks: {len(timestamps)}") 
                    buffer.extend(
                        [f"{unixTime},{timestamps[i]}" + "".join(f",{e:.8f}" for e in chunk[i]) + "\n"
                         for i in range(len(timestamps))]
                    )

                if len(buffer) >= buffer_size:
                    print(f"   Append Data to File (in thread)    ")
                    write_queue.put("".join(buffer))
                    buffer.clear()  

                if keyboard.is_pressed('/'):
                    break
                
                # Optional: sleep to prevent overloading CPU ??
                # time.sleep(0.01)

            except Exception as e:
                print(f"Error occurred: {e}")
                break
    finally:
        # Put remaaawf awining buffer into the queue before exiting
        if buffer:
            write_queue.put("".join(buffer))

        # Signal the writer thread to stop and wait for it to finish
        stop_event.set()
        writer_thread.join()

if __name__ == "__main__":
    main()


# Copy this code to run
# & conda run --live-stream --name base python c:/Users/Display/Desktop/Kim-MT/eegFile.py

