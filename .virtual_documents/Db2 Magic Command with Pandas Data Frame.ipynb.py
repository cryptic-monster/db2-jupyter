get_ipython().getoutput("wget https://raw.githubusercontent.com/IBM/db2-jupyter/master/db2.ipynb")


get_ipython().run_line_magic("run", " db2.ipynb")


get_ipython().run_line_magic("sql", " CONNECT TO bludb USER user1013 USING ppppppp HOST host.or.ip PORT 50000;")


db2indexs_list = get_ipython().run_line_magic("sql", " -r select * from syscat.indexes ")
nbr_cols = len(db2indexs_list) - 1
print('ROW COUNT', len(db2indexs_list))
print('COLUMN COUNT',len(db2indexs_list[0]))
print(type(db2indexs_list))
print(db2indexs_list[0:3])


import pandas as pd
db2indexes_df = pd.DataFrame(db2indexs_list)
print(db2indexes_df.shape)
db2indexes_df.head()


db2indexs_list = get_ipython().run_line_magic("sql", " -r select indname, tabname, tabschema, uniquerule, colcount, \")
                                pctfree, nlevels, stats_time, compression \
                           from syscat.indexes \
                          where TABSCHEMA not like 'SYSget_ipython().run_line_magic("'", " \")
                            and TABSCHEMA not like 'IBMget_ipython().run_line_magic("'", " ")
nbr_cols = len(db2indexs_list) - 1
print('ROW COUNT', len(db2indexs_list))
print('COLUMN COUNT',len(db2indexs_list[0]))
print(type(db2indexs_list))
db2indexes_df = pd.DataFrame(db2indexs_list)
print(db2indexes_df.shape)
db2indexes_df.head()


get_ipython().run_line_magic("sql", " connect reset;")



