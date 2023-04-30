Instalattion:
   1. Create DB environment
         Execute the DDL.sql in "db" folder
   2. Prepare the Python environment
         Execute in "python_task" folder:
         
            pip install -r requirements.txt
            
               or 
               
            pip install "fastapi[all]"
            pip install psycopg2

   3. Start the application
         Execute in "python_task" folder:
         
            uvicorn main:app --reload


   Information for the end-pints can be found in:
   
      http://localhost:8000/docs
