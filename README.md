# Shopify Developer Intern Challenge Question

My answer to this challenge was to build a simple Flask (CLI) API for clients to upload and organize their personal images 
into digital folders. Note that this API deals with pseudo-images, where the images are stored as strings and not actual 
image files.

## Installation

1. Clone this repository
2. Install the packages listed in ```requirements.txt```
3. Use the Node Package Manager to install dynalite (this will allow us to interact with dynamo locally):
```bash
npm install -g dynalite
```

## Usage

To use the API locally, you must:
1. Open a terminal window and enter: ```dynalite --port 800``` (this gives you a DynamoDB compatible server running 
on port 8000).
2. Open a second terminal window and enter: ```flask run``` (this starts the flask app)
3. Open a third terminal window to interact with the CLI

Now that you have set up the proper environment, you may use the app! Below is an example usage:

```bash
$ flask get overview
No active folders

$ flask upload folder A
$ flask upload folder B
$ flask upload folder C
$ flask get overview
A: []
B: []
C: []

$ flask upload image test.jpg A
$ flask upload image sample.png B
$ flask upload image test.jpg C
$ flask get overview
A: ['test.jpg']
B: ['sample.png']
C: ['test.jpg']

$ flask delete image test.jpg A
$ flask get overview
A: []
B: ['sample.png']
C: ['test.jpg']

$ flask delete folder B
$ flask get overview
A: []
C: ['test.jpg']

$ flask delete all
$ flask get overview
No active folders

```

## Endpoints/Commands

Upload a folder : ```flask upload folder <folder_title>```

Delete a folder (and all the images inside of it) : ```flask delete folder <folder_title>```

Upload an image inside a folder : ```flask upload image <image_title> <folder_title>```

Delete an image inside a folder : ```flask delete image <image_title> <folder_title>```

Delete all folders and images : ```flask delete all```

Get active folders : ```flask get folders```

Get active images (from all folders) : ```flask get images```

Get all images from a folder : ```flask get image_from_folder <folder_name>```

Get a summary of the current status of the image repository : ```flask get overview```