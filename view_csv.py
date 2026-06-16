import pandas as pd
import os
import webbrowser
from pathlib import Path
import json

# Path to the data folder
data_folder = r"C:\Users\kimbe\iCloudDrive\Master\Masterarbeit\Experiment-V2\data"

# Check if data folder exists
if not os.path.exists(data_folder):
    print(f"Error: Data folder not found at {data_folder}")
    exit()

# Find all CSV files in the data folder
csv_files = []
for filename in os.listdir(data_folder):
    if filename.endswith('.csv'):
        file_path = os.path.join(data_folder, filename)
        file_size = os.path.getsize(file_path) / 1024  # Size in KB
        csv_files.append({
            'name': filename,
            'path': file_path,
            'size': file_size
        })

# Sort by name
csv_files.sort(key=lambda x: x['name'])

if not csv_files:
    print(f"Error: No CSV files found in {data_folder}")
    exit()

print(f"Found {len(csv_files)} CSV files")
print("Creating web viewer...")

# Create a data structure for all CSV files
csv_data = {}
for file_info in csv_files:
    try:
        df = pd.read_csv(file_info['path'])
        csv_data[file_info['name']] = {
            'html': df.to_html(classes='display', table_id='csvTable', index=False, escape=False),
            'rows': len(df),
            'columns': len(df.columns),
            'column_names': df.columns.tolist()
        }
    except Exception as e:
        csv_data[file_info['name']] = {
            'error': str(e)
        }

# Create HTML with file selector
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CSV Viewer - Interactive File Selector</title>
    <link rel="stylesheet" href="https://cdn.datatables.net/1.13.6/css/jquery.dataTables.min.css">
    <script src="https://code.jquery.com/jquery-3.7.0.min.js"></script>
    <script src="https://cdn.datatables.net/1.13.6/js/jquery.dataTables.min.js"></script>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, sans-serif;
            margin: 0;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            max-width: 100%;
            margin: 0 auto;
            background: white;
            padding: 30px;
            border-radius: 8px;
            box-shadow: 0 2px 8px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #333;
            margin-top: 0;
            font-size: 28px;
            display: flex;
            align-items: center;
            gap: 10px;
        }}
        .file-selector {{
            background: #f8f9fa;
            padding: 20px;
            border-radius: 6px;
            margin-bottom: 25px;
            border: 2px solid #e0e0e0;
        }}
        .file-selector label {{
            font-weight: 600;
            color: #333;
            margin-bottom: 10px;
            display: block;
            font-size: 16px;
        }}
        .file-selector select {{
            width: 100%;
            padding: 12px;
            border: 2px solid #ddd;
            border-radius: 6px;
            font-size: 15px;
            background-color: white;
            cursor: pointer;
            transition: border-color 0.3s;
        }}
        .file-selector select:hover {{
            border-color: #0066cc;
        }}
        .file-selector select:focus {{
            outline: none;
            border-color: #0066cc;
            box-shadow: 0 0 0 3px rgba(0, 102, 204, 0.1);
        }}
        .info {{
            background: #e8f4f8;
            padding: 15px;
            border-radius: 4px;
            margin-bottom: 20px;
            border-left: 4px solid #0066cc;
            display: none;
        }}
        .info.active {{
            display: block;
        }}
        .info-item {{
            margin: 5px 0;
            color: #555;
        }}
        .table-container {{
            display: none;
        }}
        .table-container.active {{
            display: block;
        }}
        table.dataTable {{
            width: 100% !important;
            margin-top: 20px !important;
        }}
        table.dataTable thead th {{
            background-color: #0066cc;
            color: white;
            font-weight: 600;
            padding: 12px 8px;
        }}
        table.dataTable tbody td {{
            padding: 10px 8px;
            border-bottom: 1px solid #ddd;
        }}
        table.dataTable tbody tr:hover {{
            background-color: #f0f8ff;
        }}
        .dataTables_wrapper .dataTables_filter input {{
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 5px 10px;
            margin-left: 8px;
        }}
        .dataTables_wrapper .dataTables_length select {{
            border: 1px solid #ddd;
            border-radius: 4px;
            padding: 5px;
            margin: 0 8px;
        }}
        .welcome {{
            text-align: center;
            padding: 40px 20px;
            color: #666;
        }}
        .welcome.hidden {{
            display: none;
        }}
        .error {{
            background: #fee;
            border-left: 4px solid #d00;
            padding: 15px;
            border-radius: 4px;
            color: #c00;
        }}
    </style>
</head>
<body>
    <div class="container">
        <h1>📊 CSV Data Viewer</h1>
        
        <div class="file-selector">
            <label for="fileSelect">Select a CSV file to view ({len(csv_files)} files available):</label>
            <select id="fileSelect">
                <option value="">-- Choose a file --</option>
                {chr(10).join([f'<option value="{i}">{file_info["name"]} ({file_info["size"]:.1f} KB)</option>' for i, file_info in enumerate(csv_files)])}
            </select>
        </div>
        
        <div class="welcome" id="welcome">
            <h2>👆 Select a CSV file from the dropdown above to begin</h2>
            <p>You can search, sort, and filter the data once loaded.</p>
        </div>
        
        <div id="infoContainer"></div>
        <div id="tableContainer"></div>
    </div>

    <script>
        const csvData = {json.dumps(csv_data)};
        const csvFiles = {json.dumps([f['name'] for f in csv_files])};
        let currentTable = null;

        document.getElementById('fileSelect').addEventListener('change', function() {{
            const index = this.value;
            const welcome = document.getElementById('welcome');
            const infoContainer = document.getElementById('infoContainer');
            const tableContainer = document.getElementById('tableContainer');
            
            if (index === '') {{
                welcome.classList.remove('hidden');
                infoContainer.innerHTML = '';
                tableContainer.innerHTML = '';
                if (currentTable) {{
                    currentTable.destroy();
                    currentTable = null;
                }}
                return;
            }}
            
            welcome.classList.add('hidden');
            const fileName = csvFiles[index];
            const data = csvData[fileName];
            
            if (data.error) {{
                infoContainer.innerHTML = `
                    <div class="error">
                        <strong>Error loading file:</strong> ${{data.error}}
                    </div>
                `;
                tableContainer.innerHTML = '';
                return;
            }}
            
            // Update info
            infoContainer.innerHTML = `
                <div class="info active">
                    <div class="info-item"><strong>File:</strong> ${{fileName}}</div>
                    <div class="info-item"><strong>Rows:</strong> ${{data.rows.toLocaleString()}}</div>
                    <div class="info-item"><strong>Columns:</strong> ${{data.columns}}</div>
                    <div class="info-item"><strong>Column Names:</strong> ${{data.column_names.join(', ')}}</div>
                </div>
            `;
            
            // Update table
            if (currentTable) {{
                currentTable.destroy();
            }}
            
            tableContainer.innerHTML = data.html;
            
            // Initialize DataTable
            currentTable = $('#csvTable').DataTable({{
                pageLength: 25,
                lengthMenu: [[10, 25, 50, 100, -1], [10, 25, 50, 100, "All"]],
                order: [],
                scrollX: true,
                language: {{
                    search: "Search all columns:",
                    lengthMenu: "Show _MENU_ entries per page",
                    info: "Showing _START_ to _END_ of _TOTAL_ entries",
                    infoEmpty: "Showing 0 to 0 of 0 entries",
                    infoFiltered: "(filtered from _MAX_ total entries)"
                }}
            }});
        }});
    </script>
</body>
</html>
"""

# Save HTML file
output_file = os.path.join(data_folder, "csv_viewer.html")
with open(output_file, 'w', encoding='utf-8') as f:
    f.write(html_content)

print(f"✓ Created HTML viewer: {output_file}")
print("✓ Opening in browser...")

# Open in default browser
webbrowser.open('file://' + os.path.abspath(output_file))

print("\n✅ Done! The CSV viewer is now open in your browser.")
print("   Select any file from the dropdown to view it interactively!")
