import os
import dash
import dash_bootstrap_components as dbc
import dash_uploader as du
from dash import dcc, html, Input, Output, State
import process
from flask import send_file

UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "Output"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def get_text_files():
    return [f for f in os.listdir(OUTPUT_FOLDER)]

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)
server = app.server  

# Configure Dash-Uploader
du.configure_upload(app, UPLOAD_FOLDER)

app.layout = dbc.Container([
    html.H2("C++ Parallel Compiler"),
    dbc.Row([
        dbc.Col(du.Upload(id="upload-file", text="Drag and drop a C++ file here",
                          text_completed="File uploaded: {filename}",
                          max_files=1), width=6, className="mb-3"),
        dbc.Col(dbc.Button("Compile", id="compile-btn", color="primary", className="mt-2"), width=3),
    ], justify="center"),
    html.Div(id="status", className="text-success mt-3 mb-4 text-center"),

    dbc.Row([
        dbc.Col([
            html.Div([
                html.Label("Select File 1:", className="fw-bold"),
                dcc.Dropdown(id="dropdown-1", options=[], placeholder="Select a text file"),
                html.Pre(id="output-1", className="pre-box mt-2")
            ], className="dropdown-container")
        ], width=4),

        dbc.Col([
            html.Div([
                html.Label("Select File 2:", className="fw-bold"),
                dcc.Dropdown(id="dropdown-2", options=[], placeholder="Select a text file"),
                html.Pre(id="output-2", className="pre-box mt-2")
            ], className="dropdown-container")
        ], width=4),

        dbc.Col([
            html.Div([
                html.Label("Select File 3:", className="fw-bold"),
                dcc.Dropdown(id="dropdown-3", options=[], placeholder="Select a text file"),
                html.Pre(id="output-3", className="pre-box mt-2")
            ], className="dropdown-container")
        ], width=4),
    ], className="mt-4"),

    dcc.Download(id="download-link")
], fluid=True)

@app.callback(
    [Output("dropdown-1", "options"),
     Output("dropdown-2", "options"),
     Output("dropdown-3", "options")],
    Input("dropdown-1", "value")  
)
def update_dropdown_options(_):
    files = get_text_files()
    options = [{"label": f, "value": f} for f in files]
    return options, options, options

@app.callback(
    Output("status", "children"),
    #Output("download-link", "data"),
    Input("compile-btn", "n_clicks"),
    State("upload-file", "isCompleted"),
    State("upload-file", "fileNames"),
    prevent_initial_call=True
)
def compile_file(n_clicks, is_completed, file_names):
    if not is_completed or not file_names:
        return "No file uploaded yet.", None

    input_file = os.path.join(get_latest_folder(), file_names[0])
    print("Input file:", input_file)
    try:
        output_file = process.run_pipeline(input_file)
        return "Compilation successful!" # Click below to download." , dcc.send_file(output_file)
    except Exception as e:
        return f"Error: {str(e)}", None

@app.callback(Output("output-1", "children"), Input("dropdown-1", "value"))
def display_file_1(filename): return read_file_content(filename)

@app.callback(Output("output-2", "children"), Input("dropdown-2", "value"))
def display_file_2(filename): return read_file_content(filename)

@app.callback(Output("output-3", "children"), Input("dropdown-3", "value"))
def display_file_3(filename): return read_file_content(filename)

def read_file_content(filename):
    if not filename:
        return "Select a file to view content."
    
    file_path = os.path.join(OUTPUT_FOLDER, filename)
    if os.path.exists(file_path):
        with open(file_path, "r", encoding="utf-8") as f:
            return f.read()
    return "File not found."

def get_latest_folder():
    """Finds the latest modified folder inside the uploads directory."""
    folders = [os.path.join(UPLOAD_FOLDER, f) for f in os.listdir(UPLOAD_FOLDER) if os.path.isdir(os.path.join(UPLOAD_FOLDER, f))]
    return max(folders, key=os.path.getmtime) if folders else None

if __name__ == "__main__":
    app.run(debug=False)
