# TBGAN-FastAPI
## IIIT Delhi Dashboard API

Note: Model used is a test model similar to actual one used in research

How to Run:
1. Run app.py file 
2. Visit http://127.0.0.1:5000/docs to see all the CRUD operations inside the API
3. Screen should look like this:
![image](https://user-images.githubusercontent.com/78900552/182476735-f190571b-8d0e-4762-8998-55f7d310ac89.png)

4. Execute the DELETE operation to remove pre-existing files (if present)
5. Execute the PUT (/load data) opertation to add .csv file then execute

Dataset used for this model: https://www.kaggle.com/datasets/brunogrisci/breast-cancer-gene-expression-cumida

![image](https://user-images.githubusercontent.com/78900552/182476975-3102256b-f4be-442f-9987-1ed2f72160b3.png)

6. Then use GET (/train) to run the model
7. output.csv file is generated after the model is run. 
8. To download use the last GET (/output) operation
![image](https://user-images.githubusercontent.com/78900552/182477518-dd586e27-8de8-4f1a-bf41-91bd6c838ee2.png)

