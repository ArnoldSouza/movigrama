# -*- coding: utf-8 -*-
"""
Created on Mon May 14 11:32:47 2018

@author: Arnold
"""


# imports
import pic  # import plot module
import funcs as fc  # import functions module
import time  # manage elapsed time

while True:
	print('●'*79) # line delimiter
	print('Stock Movement analysis - Movigrama')
	print('●'*79) # line delimiter

	# TODO delete in future
	# parameters = {'filial': "'02'",
				  # 'armazem': "'21'",
				  # 'codigo': "'02500727'",
				  # 'intervalo': -365}

	# put values into variables of the SQL query
	# TODO uncomment in future
	parameters = fc.get_params('filial', 'armazem', 'codigo', 'intervalo')

	# get inicial time
	start_time = time.time()
	print('starting aplication at: {}h local'
		  .format(time.strftime("%H:%M:%S", time.localtime(start_time))),
		  end='\n'*2)

	# Open and read the file as a single buffer
	sqlFile = fc.read_sql_file('DATAFRAME')

	sqlFile = sqlFile.format(**parameters)

	# open database connection
	conn = fc.connect()

	# query the database server
	df = fc.fetch_data(sqlFile, conn, action=False)  # TODO remember change action

	# get complements of information to build the chart
	complements = fc.get_complements(conn,
									 parameters,
									 'product',
									 'warehouse',
									 'last_stock')

	# close the database connection
	conn.close()

	# add the recalculation of Stock Level Column
	df = fc.cumulative_inverse_sum(df, complements['last_stock'])

	# function to plot the graph
	pic.assembly_chart(df, complements)

	# end of application
	elapsed_time = time.time() - start_time
	print('\n', 'application finished (hh:mm:ss): {}'
		  .format(time.strftime("%H:%M:%S", time.gmtime(elapsed_time))), sep='', end='\n'+'-'*79+'\n'*2)
