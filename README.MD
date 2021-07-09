# **Fast Api Multischemas**
Dummy API to understand the do's and dont's of Fast API
#

### **Installation**
##
#### 1 - Create a virtual environment
```sh
python -m venv env
```

#### 2 - Activate your virtual environment
##
Linux 
```sh
source env/bin/activate
```
##
Windows
```cmd
env\Scripts\activate
```

#### 3 - Install project requirements
##

```sh
pip install -r requirements.txt
```
#
### **Running the project**
To run the project on your localhost it's necessary to have a local PostgreSQL instance. Database properties defined in:
```sh
src/database.py
```
## 
After checking the configurations and etc, you can finally run the project:
> **Note:** Check the documentation for further information regarding [database configuration on fast api](https://fastapi.tiangolo.com/tutorial/sql-databases/).

```sh
uvircorn src.main:app
```

### **Project goals**:
- [ ] Run with docker
- [x] Multi-tenancy on PSQL Schemas
- [ ] Middleware implementation (Authentication and Schema directioner)
- [ ] Unit tests





