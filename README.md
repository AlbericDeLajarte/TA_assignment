# TA_assignment

## Description
This repository solve the assignement problem in the case of a list of tasks to be distributed among several assistants.
- Each assistant has already worked a certain amount of time, which is described in the file `data/TA.csv`.
- Each task takes a certain amount of time to be solved, which is described in the file `data/tasks.csv`

The goal of the solver is to distribute the tasks among the assistants such that each assistant has the same total workload.
The resulting assignement will be printed in the console and saved in `data/assignement.csv`.

## Installation
Install all the packges:
```
pip install -r requirements.txt
```

Then visit [Mosek license page](https://www.mosek.com/products/academic-licenses/) to get your academic license by mail.
Place the license file `mosek.lic` in `/home/YOUR_USER_NAME/mosek/mosek.lic` (or just follow their instructions it's super simple!)
