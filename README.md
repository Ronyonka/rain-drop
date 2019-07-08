# RainDrop
#### Date of Current Version (July 8th,2019)
#### By **Ron Onyonka**
## Description
This is an app that takes in user data on rainfall and displays it on a chart


## Behaviour Driven Development
| Behaviour     | Input     | Output  |
| ------------- |:-------------:| -----:|
| Add rainfall Data| Users adds amount of rainfall in mm and the specific date| data is taken in and displayed on the chart |
| Filter dates | User selects a range of dates for data they need| the data on the graph is then displayed for the selected range  |


## Link to Live Website 
Here is a link to the live website: <https://rondrop.herokuapp.com/>


### Technologies Used

- HTML
- CSS
- Python(Django Framework)
- Chart.js
- Django

## Setup/Installation Requirements


### Prerequisites
You need the following to work on the project: -
* Python version 3
* Pip 
* venv 
* A text Editor
* git

### Clone the repo and check into the project folder

- `git clone https://github.com/Ronyonka/rain-drop`
- `cd rain-drop`

### Create and activate the virtual environment

- `$ python -m venv venv`
- `$ source venv/bin/activate` or `venv\scripts\activate`(Windows)



### Install the dependencies found in the  requirements.txt file

```bash
(virtual)$ pip install -r requirements.txt
```



### Make migrations


- `(virtual)$ python manage.py makemigrations `
- `(virtual)$ pytohon3.6 manage.py migrate`


### Run `manage.py` in the terminal

```bash
(virtual)$ python manage.py runserver
```

## Known Bugs
- Currently not responsive on different screen sizes. Currently working on that.

## License
MIT License

Copyright (c) 2019 Ron Onyonka

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sub-license, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.