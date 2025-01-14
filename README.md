# Employee Retention Prediction - (ML and Django)

## Overview
Employee retention is a critical challenge for organizations striving to maintain a talented workforce. This project predicts whether an employee is likely to look for a job change based on specific input features.

## Features
- **Data Analysis**: Cleaned and analyzed employee data to identify significant factors influencing retention.
- **Machine Learning Model**: Built a predictive model using Random Forest Algorithm
- **Web Application**: Developed a user-friendly interface with Django to interact with the model.
- **Local Deployment**: Designed for running locally on a development server.

## Local Deployment
Run the project locally by following the steps below:

1. Clone the repository:
   ```bash
   git clone https://github.com/shreyashnarvekar/Employee-Retention-Prediction---ML-and-Django.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Employee-Retention-Prediction---ML-and-Django
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```
4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the Django development server:
   ```bash
   python manage.py runserver
   ```
6. Access the app locally at `http://127.0.0.1:8000/`.

## Usage
1. Open the application in your web browser.
2. Fill out the form with the required features, such as:
   - **City**
   - **Training hours**
   - **Other relevant employee details**
3. Submit the form to get a prediction on whether the employee is likely to look for a job change.
4. View the result, which provides a "Yes" or "No" answer based on the prediction.

## Project Structure
```
├── dataset
│   ├── aug_train.csv       # Dataset used for training
├── models
│   ├── ml_model.sav        # Trained machine and Prediction
│   └── scaler.sav          # Feature Scaling
├── webapp
│   ├── templates
|   |   └── base.html       # CDN, Navbar and Footer
│   │   └── index.html      # FORM
│   |   └── result.html     # Display Prediction
│   └── views.py            # Backend logic
├── requirements.txt        # Python dependencies
├── manage.py               # Django management script
└── README.md               # Project documentation
```

## Technologies Used
- **Backend**: Django
- **Machine Learning**: Scikit-learn, Random Forest, Pandas, NumPy
- **Frontend**: HTML, CSS, Bootstrap

## Dataset
The project uses a dataset with features such as:
- city: City code
- citydevelopmentindex: Developement index of the city (scaled)
- gender: Gender of enrolee
- relevent_experience: Relevent experience of enrolee
- enrolled_university: Type of University course enrolled if any
- education_level: Education level of enrolee
- major_discipline :Education major discipline of enrolee
- experience: Enrolee total experience in years
- company_size: No of employees in current employer's company
- company_type : Type of current employer
- lastnewjob: Difference in years between previous job and current job
- training_hours: training hours completed

## Model Performance
| Metric        | Score        |
|---------------|--------------|
| Accuracy      | 82%          |
| Precision     | 82%          |
| Recall        | 81%          |
| F1-Score      | 82%          |

## Future Improvements
- Add more advanced models for better prediction.
- Implement role-based authentication for HR teams.
- Integrate data visualization dashboards.
- Support multiple languages in the interface.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests for improvements.

## Contact
For any questions or feedback, contact:
**Shreyash Narvekar**  
[LinkedIn](https://www.linkedin.com/in/shreyashnarvekar) | [GitHub](https://github.com/shreyashnarvekar)
