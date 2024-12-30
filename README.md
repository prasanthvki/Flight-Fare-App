# Flight Fare Prediction App - Setup Guide

This document provides step-by-step instructions to set up and run the Flight Fare Prediction App locally.

---

## Prerequisites

Ensure you have the following software installed on your machine:

1. **Python 3.10+**
2. **Git** (optional)
3. **pip** (Python package manager)

---

## Steps to Set Up the Application

### 1. Download the Project Files

The project files are hosted on OneDrive. Download them using the following link:
[OneDrive Download Link](https://bitsiserlohn-my.sharepoint.com/:f:/r/personal/prasanth_kizhakkedath_ue-germany_de/Documents/Machine%20Learning%20Final%20Project?csf=1&web=1&e=nrSR6J).

After downloading, the files should include:

- `flight_prediction/` (Backend folder)
- `frontend/` (Frontend folder)
- `Data_Train.xlsx` (Dataset for training)
- `flight_price.ipynb` (Jupyter notebook for model training)
- `flight_rf.pkl` (Trained model file)
- `get-pip.py` (Script to install pip if not already installed)
- `requirement.txt` (Dependencies for the project)

---

### 2. Set Up Jupyter Notebook

To work with the Jupyter Notebook:

1. **Create a Virtual Environment:**
   - Navigate to the project directory:
     ```bash
     cd your_project_directory
     ```
   - Create a virtual environment:
     ```bash
     python -m venv env
     ```
   - Activate the virtual environment:
     - On Windows:
       ```bash
       .\env\Scripts\activate
       ```
   
    

   **OR**

   **Use the Anaconda Base Environment:**
   - If you prefer, you can use your Anaconda base environment instead of creating a virtual environment.

2. Install the required dependencies:
   ```bash
     pip install -r requirements.txt
     ```
3. Open the notebook:
   ```bash
   jupyter notebook
   ```
4. Run `flight_price.ipynb` to create and train the model.
   - **Note:** Ensure that the path to `Data_Train.xlsx` is correctly configured in the notebook.

---

### 3. Run the Web Application

If you need to run the web application:

1. **Activate the provided environment:**
   - Navigate to the project directory and activate the environment named `env` :
     - On Windows:
       ```bash
       .\env\Scripts\activate
       ```

2. **Ensure the Trained Model File is in Place:**
   - The `flight_rf.pkl` file must be placed in the project folder as it is used by the backend to fetch results based on frontend inquiries. This file is obtained from the Jupyter notebook after training the model (`flight_price.ipynb`).
   

3. **Run the Backend:**
   - Navigate to the `flight_prediction` folder:
     ```bash
     cd flight_prediction
     ```
   - Start the backend server:
     ```bash
     python manage.py runserver
     ```

4. **Run the Frontend:**
   - Navigate to the `frontend` folder:
     ```bash
     cd frontend
     ```
   - Install dependencies:
     ```
     npm install
     ```
   - Start the frontend application:
     ```bash
     npm start
     ```

5. **Testing the Application:**
   - Open the UI in your browser (URL will be displayed in the terminal) and test with input values.

---

### 4. Clone the Repository (Optional)

If needed, you can clone the GitHub repository instead of downloading files from OneDrive:

```bash
git clone https://github.com/prasanthvki/Flight-Fare-App.git
cd Flight-Fare-App
```

---

## Additional Notes

1. Ensure your Python interpreter in VS Code (or your IDE) is set to the virtual environment.
2. Add any new dependencies to the `requirements.txt` file using:
   ```bash
   pip freeze > requirements.txt
   ```
3. Ensure the path to `Data_Train.xlsx` in the notebook is correctly set for smooth operation.

   ```

---

## Troubleshooting

1. **Module Not Found Error:** Ensure all dependencies are installed by re-running:
   ```bash
   pip install -r requirements.txt
   ```
2. **Jupyter Kernel Issues:** Add the virtual environment to Jupyter:
   ```bash
   python -m ipykernel install --user --name=env --display-name "Python (env)"
   ```

---



