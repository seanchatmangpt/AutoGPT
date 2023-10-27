# import necessary libraries
import asyncio
import os
import sys

# define async function
async def async_directory_walk(path):
    """
    Asynchronously walks through a given directory and returns a list of all files and subdirectories.

    Args:
        path (str): The path of the directory to be walked through.

    Returns:
        list: A list of all files and subdirectories in the given directory.
    """
    # create empty list to store results
    results = []
    
    # use asyncio.to_thread to iterate through all files and directories in given path
    async for root, dirs, files in asyncio.to_thread(os.walk, path):
        # loop through all subdirectories
        for dir in dirs:
            # add subdirectory path to results list
            results.append(os.path.join(root, dir))
        # loop through all files
        for file in files:
            # add file path to results list
            results.append(os.path.join(root, file))
            
    # return results list
    return results


# define main function
def main():
    """
    Main function that gets the path from command line arguments, runs the async_directory_walk function, and prints the results.
    """
    # get path from command line arguments
    path = sys.argv[1]
    
    # run async function and get results
    results = asyncio.run(async_directory_walk(path))
    
    # print results
    print(results)


# run main function
if __name__ == "__main__":
    main()
