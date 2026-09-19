##################################################################################
# The  test_run.py file is designed to execute an asynchronous workflow by calling the 
# run_incident() method from the runner object. It waits for the result and then prints 
# it to the console. This structure is typical for applications that require non-blocking 
# I/O operations, allowing other tasks to run concurrently while waiting for the result of run
##################################################################################

#The code imports the asyncio library, which is used for writing concurrent code using the async/await syntax.
import asyncio

#It also imports runner from the workflow_runner module located in the app.services package. This likely contains methods for managing workflows.
from app.services.workflow_runner import runner


# An asynchronous function main() is defined. Inside this function, it calls runner.run_incident() 
# using await, which means it will wait for this asynchronous operation to complete before proceeding.
# After obtaining the result, it prints a separator line and then the result itself.

async def main():

    result = await runner.run_incident()

    print("\n========== RESULT ==========\n")

    print(result)


#This line runs the main() function using asyncio.run(), which is a high-level API for running asynchronous code.
asyncio.run(main())