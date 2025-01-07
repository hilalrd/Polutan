# Extract and Visualize CO Data

This repository contains scripts and dependencies to extract and visualize carbon monoxide (CO) data from NetCDF files, specifically for the DKI Jakarta region. The output includes a CO concentration distribution plot saved as an image file.

## Files in This Repository

1. **Extract_Data_Auto.py**
   - Python script to automatically locate `.nc` and `.shp` files in the repository folder.
   - Extracts CO data and generates a visualization for the DKI Jakarta area.
   - Saves the plot as `CO_Distribution_DKI_Jakarta.png`.

2. **requirements.txt**
   - List of Python dependencies required to run the script.

## Setup and Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/hilalrd/Polutan.git
   cd your-repo-name
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure the folder contains the required input files:
   - A NetCDF file (`.nc`) with CO data.
   - A shapefile (`.shp`) representing the DKI Jakarta region.

2. Run the script:
   ```bash
   python Extract_Data_Auto.py
   ```

3. The script will:
   - Automatically locate `.nc` and `.shp` files in the current folder.
   - Extract CO data for DKI Jakarta.
   - Save the visualization as `CO_Distribution_DKI_Jakarta.png` in the same folder.

## Output

- **CO_Distribution_DKI_Jakarta.png**: A map showing the distribution of CO concentrations over the DKI Jakarta region.

## Example

After running the script, the output file `CO_Distribution_DKI_Jakarta.png` will look similar to this:

*(Include an example image here if available)*

---

If you encounter any issues or have questions, feel free to open an issue in this repository.

