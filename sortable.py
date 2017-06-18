# This Python file uses the following encoding: utf-8
import os.path
import json
import io

productDataFileName = "files/products.txt"
listingDataFileName = "files/listings.txt"
resultDataFileName = "files/results.txt"

"""**********************************************************
* errorhandler : Prints user friendly error to the console
* @param 
*    fileName -  The filename where error occurred
*    e  - The exact error
* @returns {null}
**********************************************************"""
def errorhandler(e, fileName):
    message = "Files not accessible \"" + str(fileName) + "\"!!! \n" + str(e)
    print (message)


"""**********************************************************
* createResultFile : Opens a file and return its handle (object)
* @param 
*    fileName -  The filename where results will be saved
* @returns {file object}*
**********************************************************"""
def createResultFile(fileName):
    try:
        resultsFile = open(fileName,"w")
        return resultsFile
    except OSError as e:
        errorhandler(e, fileName)

"""**********************************************************
* matchAndExtractListing : Opens listings.txt. 
*   Checks product model and manufacturer against listings.
*   Writes matching listing data to results.txt
* @param 
*    listingsFile -  The filename where listings are located
*    productManufacturer -  The product manufacturer to match
*    productModel -  The product model to match
*    resultsFile -  The resultsFile object
* @returns {null}
**********************************************************"""
def matchAndExtractListing(listingsFile, productManufacturer, productModel, resultsFile):
    listingsFile.seek(0)
    for listing in listingsFile:
        listingJSON = json.loads(listing)
        listingTitle = listingJSON['title']
        if productManufacturer and productModel in listingTitle.split():
            resultDict['listings'].append(listingJSON)
    if not resultsFile.closed:
        resultsFile.write(json.dumps(resultDict) + "\n")

        

if os.path.isfile(productDataFileName) and os.path.isfile(listingDataFileName):
    try:
        with io.open(productDataFileName, "r", encoding="utf-8") as productsFile, \
                io.open(listingDataFileName, "r", encoding="utf-8") as listingsFile:
            resultsFile = createResultFile(resultDataFileName)

            print("Record linking in progess. PLEASE WAIT!")

            # Reads product.txt line by line to improve memory usage and overall performance
            for product in productsFile:
                productJSON = json.loads(product)
                productName = productJSON['product_name']
                productManufacturer = productJSON['manufacturer']
                productModel = productJSON['model']
                resultDict = {"product_name": productName, "listings": []}

                matchAndExtractListing(listingsFile, productManufacturer, productModel, resultsFile)

            listingsFile.close()
            print("All done. THANK YOU!")
    except OSError as e:
        errorhandler(e, productDataFileName)
else:
    print("Files not found!")


