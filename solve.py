import cvxpy as cp
import numpy as np
import pandas as pd
import os

dirname = os.path.dirname(__file__)

# List of tasks and their workloads
tasks = pd.read_csv(os.path.join(dirname, 'data', 'tasks.csv'))
work_task = tasks['worload [min]'].astype(int)

# List of teaching assistants (TA) and their workloads
assistants = pd.read_csv(os.path.join(dirname, 'data', 'TA.csv'))
work_assistants = assistants['workload [min]'].astype(int)

NTASK = len(work_task)
NAGENT = len(work_assistants)

# Optimization problem
total_work = np.sum(work_task) + np.sum(work_assistants)

x = cp.Variable((NAGENT,NTASK),boolean=True, integer=True)
objective = cp.Minimize(cp.sum_squares(  (cp.sum(cp.multiply(x, np.tile(work_task, (NAGENT,1))), axis=1)+work_assistants-total_work)  ))

prob = cp.Problem( objective,
                  [cp.sum(x,axis=0) == 1, 
                   cp.sum(x,axis=1) >= 0])

# solve and print results
res = prob.solve(solver='MOSEK', verbose=True)
print(prob.status)

# save results
df = pd.DataFrame(columns=['TA','Task','Total workload [min]'])
for i in range(NAGENT):
    df.loc[len(df)] = [assistants['name'][i], 
                       (tasks['name'][np.where(x.value[i])[0]]).tolist(), 
                       (x.value[i]*work_task).sum() + work_assistants[i]]

print(df)
df.to_csv(os.path.join(dirname, 'data', 'assignment.csv'), index=False)
