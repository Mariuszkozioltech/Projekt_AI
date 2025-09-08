# Automate the Boring Stuff with Python

![obrazek](/images/cover-automate3-thumb.webp)
![obrazek](/images/cover-bigbookpython-thumb.webp)
![obrazek](/images/cover-beyond-thumb.webp)
![obrazek](/images/cover-invent4th-thumb.webp)
![obrazek](/images/cover-crackingcodes-thumb.webp)

## B
ANSWERS TO THE PRACTICE QUESTIONS

![obrazek](images/000112.jpg)
This appendix contains the answers to the practice questions at the end of each chapter. I highly recommend that you take the time to work through these questions. Programming is more than memorizing syntax and a list of function names. As when learning a foreign language, the more practice you put into it, the more you will get out of it. There are many websites with practice programming questions as well.
When it comes to the practice programs, there is no one correct solution. As long as your program performs what the project asks for, you can consider it correct. However, if you want to see examples of completed projects, they are available in the “Download the files used in this book” link at https://nostarch.com/automate-boring-stuff-python-3rd-edition.

## Chapter 1

1.  The operators are +, -, *, and /. The values are 'hello', -88.8, and 5.
2.  The string is 'spam'; the variable is spam. Strings always start and end with quotes.
3.  The three data types introduced in this chapter are integers, floating-point numbers, and strings.
4.  An expression is a combination of values and operators. All expressions evaluate (that is, reduce) to a single value.
5.  An expression evaluates to a single value. A statement does not.
6.  The bacon variable is set to 20. The bacon + 1 expression does not reassign the value in bacon (that would need an assignment statement: bacon = bacon + 1).
7.  Both expressions evaluate to the string 'spamspamspam'.
8.  Variable names cannot begin with a number.
9.  The int(), float(), and str() functions will evaluate to the integer, floating-point number, and string versions of the value passed to them.
10.  The expression causes an error because 99 is an integer, and only strings can be concatenated to other strings with the + operator. The correct way is I have eaten ' + str(99) + ' burritos.'
1.  True and False, using capital T and F, with the rest of the word in lowercase.
2.  and, or, and not
3.  True and True is True.
True and False is False.
False and True is False.
False and False is False.
True or True is True.
True or False is True.
False or True is True.
False or False is False.
not True is False.
not False is True.
4.  False
False
True
False
False
True
5.  ==, !=, <, >, <=, and >=
6.  == is the equal to operator that compares two values and evaluates to a Boolean, while = is the assignment operator that stores a value in a variable.
7.  A condition is an expression used in a flow control statement that evaluates to a Boolean value.
8.  The lines print('bacon') and print('ham') are each blocks by themselves, and a third block is everything after if spam == 10: and before the final print('Done'):

```
print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
print('spam')
```


```
print('eggs')
if spam > 5:
    print('bacon')
else:
    print('ham')
print('spam')
```

9.  The code:

```
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
```


```
if spam == 1:
    print('Hello')
elif spam == 2:
    print('Howdy')
else:
    print('Greetings!')
```

1.  Press CTRL-C to stop a program stuck in an infinite loop.
2.  The break statement will move the execution outside and just after a loop. The continue statement will move the execution to the start of the loop.
3.  They all do the same thing. The range(10) call ranges from 0 up to (but not including) 10, range(0, 10) explicitly tells the loop to start at 0, and range(0, 10, 1) explicitly tells the loop to increase the variable by 1 on each iteration.
4.  The code:

```
for i in range(1, 11):
    print(i)
```


```
for i in range(1, 11):
    print(i)
```

and:

```
i = 1
while i <= 10:
    print(i)
    i = i + 1
```


```
i = 1
while i <= 10:
    print(i)
    i = i + 1
```

5.  This function can be called with spam.bacon().
1.  Functions reduce the need for duplicate code. This makes programs shorter, easier to read, and easier to update.
2.  The code in a function executes when the function is called, not when the function is defined.
3.  The def statement defines (that is, creates) a function.
4.  A function consists of the def statement and the code in its def clause. A function call is what moves the program execution into the function, and the function call evaluates to the function’s return value.
5.  There is one global scope, and a local scope is created whenever a function is called.
6.  When a function returns, the local scope is destroyed, and all the variables in it are forgotten.
7.  A return value is the value that a function call evaluates to. Like any value, a return value can be used as part of an expression.
8.  If there is no return statement for a function, its return value is None.
9.  A global statement will force a variable in a function to refer to the global variable.
10.  The data type of None is NoneType.
11.  That import statement imports a module named areallyourpetsnamederic. (This isn’t a real Python module, by the way.)
12.  This function can be called with spam.bacon().
13.  Place the line of code that might cause an error in a try clause.
14.  The code that could potentially cause an error goes in the try clause. The code that executes if an error happens goes in the except clause.
15.  The random_number global variable is set once to a random number, and the random_number variable in the get_random_dice_roll() function uses the global variable. This means the same number is returned for every get _random_dice_roll() function call.
1.  assert spam >= 10, 'The spam variable is less than 10.'
2.  Either assert eggs.lower() != bacon.lower() 'The eggs and bacon variables are the same!' or assert eggs.upper() != bacon.upper(), 'The eggs and bacon variables are the same!'
3.  assert False, 'This assertion always triggers.'
4.  To be able to call logging.debug(), you must have these two lines at the start of your program:

```
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
%(levelname)s - %(message)s')
```


```
import logging
logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -
%(levelname)s - %(message)s')
```

5.  To be able to send logging messages to a file named programLog.txt with logging.debug(), you must have these two lines at the start of your program:

```
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
format=' %(asctime)s - %(levelname)s - %(message)s')
```


```
import logging
logging.basicConfig(filename='programLog.txt', level=logging.DEBUG,
format=' %(asctime)s - %(levelname)s - %(message)s')
```

6.  DEBUG, INFO, WARNING, ERROR, and CRITICAL
7.  logging.disable(logging.CRITICAL)
8.  You can disable logging messages without removing the logging function calls. You can selectively disable lower-level logging messages. You can create logging messages. Logging messages provides a timestamp.
9.  The Step In button will move the debugger into a function call. The Step Over button will quickly execute the function call without stepping into it. The Step Out button will quickly execute the rest of the code until it steps out of the function it currently is in.
10.  After you click Continue, the debugger will stop when it has reached the end of the program or a line with a breakpoint.
11.  A breakpoint is a setting on a line of code that causes the debugger to pause when the program execution reaches the line.
12.  To set a breakpoint in Mu, click the line number to make a red dot appear next to it.
1.  The empty list value, which is a list value that contains no items. This is similar to how '' is the empty string value.
2.  spam[2] = 'hello' (Notice that the third value in a list is at index 2 because the first index is 0.)
3.  'd' (Note that '3' * 2 is the string '33', which is passed to int() before being divided by 11. This eventually evaluates to 3. Expressions can be used wherever values are used.)
4.  'd' (Negative indexes count from the end.)
5.  ['a', 'b']
6.  1
7.  [3.14, 'cat', 11, 'cat', True, 99]
8.  [3.14, 11, 'cat', True]
9.  The operator for list concatenation is +, while the operator for replication is *. (This is the same as for strings.)
10.  While append() will add values only to the end of a list, insert() can add them anywhere in the list.
11.  The del statement and the remove() list method are two ways to remove values from a list.
12.  Both lists and strings can be passed to len(), have indexes and slices, be used in for loops, be concatenated or replicated, and be used with the in and not in operators.
13.  Lists are mutable; they can have values added, removed, or changed. Tuples are immutable; they cannot be changed at all. Also, tuples are written using parentheses, (and), while lists use square brackets, [and].
14.  (42,) (The trailing comma is mandatory.)
15.  The tuple() and list() functions, respectively.
16.  They contain references to list values.
17.  The copy.copy() function will do a shallow copy of a list, while the copy.deepcopy() function will do a deep copy of a list. That is, only copy .deepcopy() will duplicate any lists inside the list.
1.  Two curly brackets: {}
2.  {'foo': 42}
3.  The items stored in a dictionary are unordered, while the items in a list are ordered.
4.  You get a KeyError error.
5.  There is no difference. The in operator checks whether a value exists as a key in the dictionary.
6.  The expression 'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks whether there is a value 'cat' for one of the keys in spam.
7.  spam.setdefault('color', 'black')
8.  pprint.pprint()
1.  Escape characters represent characters in string values that would otherwise be difficult or impossible to type into code.
2.  The \n escape character is a newline; the \t escape character is a tab.
3.  The \\ escape character will represent a backslash character.
4.  The single quote in Howl's is fine because you’ve used double quotes to mark the beginning and end of the string.
5.  Multiline strings allow you to use newlines in strings without the \n escape character.
6.  The expressions evaluate to the following:
'e'
'Hello'
'Hello'
'lo world!
7.  The expressions evaluate to the following:
'HELLO'
True
'hello'
8.  The expressions evaluate to the following:
['Remember,', 'remember,', 'the', 'fifth', 'of', 'November.']
'There-can-be-only-one.'
9.  The rjust(), ljust(), and center() string methods, respectively.
10.  The lstrip() and rstrip() methods remove whitespace from the left and right ends of a string, respectively.
1.  The re.compile() function creates Regex objects.
2.  Raw strings are used so that backslashes do not have to be escaped.
3.  The search() method returns Match objects.
4.  The group() method returns strings of the matched text.
5.  Group 0 is the entire match, group 1 covers the first set of parentheses, and group 2 covers the second set of parentheses.
6.  Periods and parentheses can be escaped with a backslash: \., \(, and \).
7.  If the regex has no groups, a list of strings is returned. If the regex has groups, a list of tuples of strings is returned.
8.  The | character signifies matching “either, or” between two groups.
9.  The ? character can either mean “match zero or one of the preceding group” or be used to signify non-greedy matching.
10.  The + matches one or more. The * matches zero or more.
11.  The {3} matches exactly three instances of the preceding group. The {3,5} matches between three and five instances.
12.  The \d, \w, and \s shorthand character classes match a single digit, word, or space character, respectively.
13.  The \D, \W, and \S shorthand character classes match a single character that is not a digit, word, or space character, respectively.
14.  The .* performs a greedy match, and the .*? performs a non-greedy match.
15.  Either [0-9a-z] or [a-z0-9].
16.  Passing re.I or re.IGNORECASE as the second argument to re.compile() will make the matching case insensitive.
17.  The . character normally matches any character except the newline character. If re.DOTALL is passed as the second argument to re.compile(), then the dot will also match newline characters.
18.  The sub() call will return the string 'X drummers, X pipers, five rings, X hens'.
19.  The re.VERBOSE argument allows you to add whitespace and comments to the string passed to re.compile().
1.  Relative paths are relative to the current working directory.
2.  Absolute paths start with the root folder, such as / or C:\.
3.  On Windows, it evaluates to WindowsPath('C:/Users/Al'). On other operating systems, it evaluates to a different kind of Path object but with the same path.
4.  The expression 'C:/Users' / 'Al' results in an error, since you can’t use the / operator to join two strings.
5.  The os.getcwd() function returns the current working directory. The os.chdir() function changes the current working directory.
6.  The . folder is the current folder, and .. is the parent folder.
7.  C:\bacon\eggs is the directory name, while spam.txt is the base name.
8.  The string 'r' for read mode, 'w' for write mode, and 'a' for append mode.
9.  An existing file opened in write mode is erased and completely overwritten.
10.  The read() method returns the file’s entire contents as a single string value. The readlines() method returns a list of strings, where each string is a line from the file’s contents.
11.  A shelf value resembles a dictionary value; it has keys and values, along with keys() and values() methods that work similarly to the dictionary methods of the same names.
1.  The shutil.copy() function will copy a single file, while shutil.copytree() will copy an entire folder, along with all its contents.
2.  The shutil.move() function is used for renaming files, as well as moving them.
3.  The send2trash function will move a file or folder to the recycle bin, while shutil will permanently delete files and folders.
4.  The zipfile.ZipFile() function is equivalent to the open() function; the first argument is the filename, and the second argument is the mode to open the ZIP file in (read, write, or append).
1.  The dir command lists folder contents on Windows. The ls command lists folder contents on macOS and Linux.
2.  The PATH environment variable contains a list of folders that are checked when a program name is entered into the terminal.
3.  The __file__ variable contains the filename of the Python script currently being run. This variable doesn’t exist in the interactive shell.
4.  The cls command clears the terminal on Windows, while the clear command does so on macOS and Linux.
5.  Run python -m venv .venv on Windows, or python3 -m venv .venv on macOS and Linux.
6.  Run python -m PyInstaller --onefile yourScript.py on Windows, or python3 -m PyInstaller --onefile yourScript.py on macOS and Linux.
1.  The webbrowser module has an open() method that will launch a web browser to a specific URL, and that’s it. The requests module can download files and pages from the web. The bs4 module parses HTML.
2.  The requests.get() function returns a Response object, which has a text attribute that contains the downloaded content as a string.
3.  The raise_for_status() method raises an exception if the download had problems and does nothing if the download succeeded.
4.  The status_code attribute of the Response object contains the HTTP status code.
5.  After opening the new file on your computer in 'wb' “write binary” mode, use a for loop that iterates over the Response object’s iter _content() method to write out chunks to the file. Here’s an example:

```
saveFile = open('filename.html', 'wb')
for chunk in res.iter_content(100000):
    saveFile.write(chunk)
```


```
saveFile = open('filename.html', 'wb')
for chunk in res.iter_content(100000):
    saveFile.write(chunk)
```

6.  Most online APIs return their responses formatted as JSON or XML.
7.  F12 brings up the developer tools in Chrome. Pressing CTRL-SHIFT-C (on Windows and Linux) or -OPTION-C (on OS X) brings up the developer tools in Firefox.
8.  Right-click the element in the page and select Inspect Element from the menu.
9.  '#main'
10.  '.highlight'
11.  spam.gettext()
12.  linkElem.attrs
13.  The selenium module is imported with from selenium import webdriver.
14.  The find_element_* methods return the first matching element as a WebElement object. The find_elements_* methods return a list of all matching elements as WebElement objects.
15.  The click() and send_keys() methods simulate mouse clicks and keyboard keys, respectively.
16.  The press('Control+A') method simulates pressing CTRL-A.
17.  The forward(), back(), and refresh() WebDriver object methods simulate these browser buttons.
18.  The go_forward(), go_back(), and reload() Page object methods simulate these browser buttons.
1.  The openpyxl.load_workbook() function returns a Workbook object.
2.  The sheetnames attribute contains a list of strings of the worksheet titles.
3.  Run wb['Sheet1'].
4.  Use wb.active.
5.  sheet['C5'].value or sheet.cell(row=5, column=3).value
6.  sheet['C5'] = 'Hello' or sheet.cell(row=5, column=3).value = 'Hello'
7.  cell.row and cell.column
8.  They hold the highest column and row with values in the sheet, respectively, as integer values.
9.  openpyxl.cell.column_index_from_string('M')
10.  openpyxl.cell.get_column_letter(14)
11.  sheet['A1':'F1']
12.  wb.save('example3.xlsx')
13.  A formula is set the same way as any value. Set the cell’s value attribute to a string of the formula text. Remember that formulas begin with the equal sign (=).
14.  Pass data_only=True when calling load_workbook() to make OpenPyXL retrieve the calculated results of formulas.
15.  sheet.row_dimensions[5].height = 100
16.  sheet.column_dimensions['C'].hidden = True
17.  Freeze panes are rows and columns that will always appear on the screen. They are useful for headers.
18.  openpyxl.chart.Reference(), openpyxl.chart.Series(), openpyxl.chart.BarChart(), chartObj.append(seriesObj), and add_chart()
1.  To access Google Sheets, you need a credentials file, a token file for Google Sheets, and a token file for Google Drive.
2.  EZSheets has ezsheets.Spreadsheet and ezsheets.Sheet objects.
3.  Call the downloadAsExcel() Spreadsheet method.
4.  Call the ezsheets.upload() function and pass the filename of the Excel file.
5.  Read the value at ss['Students']['B2'].
6.  Call ezsheets.getColumnLetterOf(999).
7.  Access the rowCount and columnCount properties of the Sheet object.
8.  Call the delete() Sheet method. This is only permanent if you pass the permanent=True keyword argument.
9.  The Spreadsheet() function and Sheet() Spreadsheet method will create Spreadsheet and Sheet objects, respectively.
10.  EZSheets will throttle your method calls.
1.  conn = sqlite3.connect('example.db', isolation_level=None)
2.  conn.execute('CREATE TABLE students (first_name TEXT, last_name TEXT, favorite_color TEXT) STRICT')
3.  Pass the isolation_level=None keyword argument when calling sqlite3.connect().
4.  While INTEGER is analogous to Python’s int type, REAL is analogous to Python’s float type.
5.  Strict mode adds a requirement that every column must have a data type, and SQLite raises an exception if you try to insert data of the wrong type.
6.  The * means “select all columns in the table.”
7.  CRUD stands for Create, Read, Update, and Delete, the four standard operations that databases perform.
8.  ACID stands for Atomic, Consistent, Isolated, and Durable, the four properties that database transactions should have.
9.  INSERT queries add new records to tables.
10.  DELETE queries delete records from tables.
11.  Without a WHERE clause, the UPDATE query applies to all records in the table, which may or may not be what you want.
12.  An index is a data structure that organizes a column’s data, which takes up more storage but makes queries faster. 'CREATE INDEX idx_birthdate ON cats (birthdate)' would create an index for the cats table’s birthdate column.
13.  A foreign key links records in one table to a record in another table.
14.  You can delete a table named cats by running the query 'DROP TABLE cats'.
15.  The string ':memory:' is used in place of a filename to create an in- memory database.
16.  The iterdump() method can create the queries to copy a database. You can also copy the database file itself.
1.  A File object must be opened in write mode by passing 'w' to open().
2.  Calling getPage(4) will return a Page object for page 5, since page 0 is the first page.
3.  Call decrypt('swordfish').
4.  Rotate pages counterclockwise by passing a negative integer: -90, -180, or -270.
5.  docx.Document('demo.docx')
6.  Use doc.paragraphs to obtain a list of Paragraph objects.
7.  A Paragraph object represents a paragraph of text and is itself made up of one or more Run objects.
8.  A Run object has these variables (not a Paragraph object).
9.  True always makes the Run object bolded and False always makes it not bolded, no matter what the style’s bold setting is. None will make the Run object just use the style’s bold setting.
10.  Call the docx.Document() function.
11.  doc.add_paragraph('Hello there!')
12.  The integers 0 through 9.
1.  In Excel, spreadsheets can have values of data types other than strings; cells can have different fonts, sizes, or color settings; cells can have varying widths and heights; adjacent cells can be merged; and you can embed images and charts.
2.  You pass a File object, obtained from a call to open().
3.  File objects need to be opened in read-binary ('rb') mode for Reader objects and write-binary ('wb') mode for Writer objects.
4.  The writerow() method.
5.  The delimiter argument changes the string used to separate cells in a row. The lineterminator argument changes the string used to separate rows.
6.  All of them can be easily edited with a text editor: CSV, JSON, and XML are plaintext formats.
7.  json.loads()
8.  json.dumps()
9.  XML’s format resembles HTML.
10.  JSON represents None values as the keyword null.
11.  Boolean values in JSON are written in lowercase: true and false.
1.  A reference moment that many date and time programs use. The moment is January 1, 1970, UTC.
2.  time.time()
3.  time.asctime()
4.  time.sleep(5)
5.  It returns the closest integer to the argument passed. For example, round(2.4) returns 2.
6.  A datetime object represents a specific moment in time. A timedelta object represents a duration of time.
7.  Run datetime.datetime(2019, 1, 7).weekday(), which returns 0. This means Monday, as the datetime module uses 0 for Monday, 1 for Tuesday, and so on, up to 6 for Sunday.
1.  The credentials.json and token.json files tell the EZGmail module which Google account to use when accessing Gmail.
2.  A message represents a single email, while a back-and-forth conversation involving multiple emails is a thread.
3.  Include the 'has:attachment' text in the string you pass to search().
4.  SMS email gateways are not guaranteed to work, don’t notify you if the message was delivered, and just because they worked before does not mean they will work again.
5.  The Requests library can send and receive ntfy notifications.
1.  An RGBA value is a tuple of four integers, each ranging from 0 to 255. The four integers correspond to the amount of red, green, blue, and alpha (transparency) in the color.
2.  Calling ImageColor.getcolor('CornflowerBlue', 'RGBA') will return (100, 149, 237, 255), the RGBA value for the cornflower blue color.
3.  A box tuple is a tuple value of four integers: the left-edge x-coordinate, the top-edge y-coordinate, the width, and the height, respectively.
4.  Image.open('zophie.png')
5.  im.size is a tuple of two integers, the width and the height.
6.  im.crop((0, 50, 50, 50)). Notice that you are passing a box tuple to crop(), not four separate integer arguments.
7.  Call the im.save('new_filename.png') method of the Image object.
8.  The ImageDraw module contains code to draw on images.
9.  ImageDraw objects have shape-drawing methods such as point(), line(), or rectangle(). They are returned by passing the Image object to the ImageDraw.Draw() function.
10.  plt.plot() creates a line graph, plt.scatter() creates a scatterplot, plt.bar() creates a bar graph, and plt.pie() creates a pie chart.
11.  The savefig() method saves the graph as an image.
12.  You cannot call plt.show() twice in a row because it resets the graph data, forcing you to run the graph-making code again if you want to show it a second time.
1.  Tesseract recognizes English by default.
2.  PyTesseract works with the Pillow image library.
3.  The image_to_string() function accepts an Image object and returns a string.
4.  No, Tesseract only extracts text from scanned documents of typewritten text and not text from photographs.
5.  tess.get_languages() returns a list of language pack strings.
6.  You can pass the lang='eng+jpn' keyword argument to identify both English and Japanese text in an image.
7.  NAPS2 can be run from a Python script to create PDFs with embedded OCR text.
1.  Move the mouse to any corner of the screen.
2.  The pyautogui.size() function returns a tuple with two integers for the width and height of the screen.
3.  The pyautogui.position() function returns a tuple with two integers for the x- and y-coordinates of the mouse cursor.
4.  The moveTo() function moves the mouse to absolute coordinates on the screen, while the move() function moves the mouse relative to the mouse’s current position.
5.  pyautogui.dragTo() and pyautogui.drag()
6.  pyautogui.typewrite('Hello world!')
7.  Either pass a list of keyboard key strings to pyautogui.write() (such as 'left') or pass a single keyboard key string to pyautogui.press().
8.  pyautogui.screenshot('screenshot.png')
9.  pyautogui.PAUSE = 2
10.  You should use Selenium for controlling a web browser instead of PyAutoGUI.
11.  PyAutoGUI clicks and types blindly and cannot easily find out if it’s clicking and typing into the correct windows. Unexpected pop-up windows or errors can throw the script off track and require you to shut it down.
12.  Call the pyautogui.getWindowsWithTitle('Notepad') function.
13.  Run w = pyatuogui.getWindowsWithTitle('Firefox'), and then run w.activate().
1.  Call engine.setProperty('rate', 300), for example, to make pyttsx3’s voice speak at 300 words per minute.
2.  The pyttsx3 module saves to the WAV audio format.
3.  No, pyttsx3 and Whisper do not require an online service or internet access.
4.  Yes, pyttsx3 and Whisper support languages other than English.
5.  Whisper’s default model is 'base'.
6.  SRT (SubRip Subtitle) and VTT Web Video Text Tracks are two common subtitle file formats.
7.  Yes, yt-dlp can download from hundreds of video websites other than YouTube.

## INDEX

Symbols
= (assignment operator), 10, 130
+= (augmented addition assignment operator), 119
/= (augmented division assignment operator), 119
%= (augmented modulus assignment operator), 119
*= (augmented multiplication assignment operator), 119
-= (augmented subtraction assignment operator), 119
\ (backslash)
escape character, 190
line continuation character, 124
path separator (Windows), 218
%* (batch file, all arguments), 276
@ (batch file, hide command), 276
{} (braces)
with dictionaries, 139
with format() method, 150
with f-strings, 164
matching a number of qualifiers, 198
^ (caret symbol)
matching beginning of string, 201
negative character classes, 193
: (colon), 34, 468
$ (dollar sign), 201
. (dot)
current folder, 222
regex, 194
.. (dot-dot) parent folder, 222
.* (dot-star), 199
" (double quotes), 160
== (equal to) operator, 29
** (exponent) operator, 6
/ (forward slash)
division operator, 6
path separator (macOS/Linux), 218
> (greater than) operator, 29
>= (greater than or equal to) operator, 29
# (hash character), 14, 204
// (integer division) operator, 6
>>> (interactive shell prompt), xli
< (less than) operator, 29
<= (less than or equal to) operator, 29
% (modulus/remainder) operator, 6
* (multiplication) operator, 6
!= (not equal to) operator, 29
() (parentheses), 6, 14, 127
| (pipe character), 191, 205
+ (plus sign)
addition operator, 6
concatenation operator, 8, 113
match one or more, 197
? (question mark)
optional match, 196
SQLite wildcard, 393
' (single quote), 8, 160
[] (square brackets), 110, 112, 123
* (star character), 197
- (subtraction) operator, 6
''' (triple quotes), 162
_ (underscore), 11, 12, 194
A
A:\ drive, 222
abs() function, 20–21
absolute() method, 224
absolute path, 222, 223
absolute value, 20
Accessibility Apps (macOS), 540
Accessible Rich Internet Applications (ARIA), 325
ACID test (Atomic Consistent Isolated Durable), 393
activate.bat (venv), 263
activate() method (PyAutoGUI), 555
active attribute (OpenPyXL), 334
active sheet, 334
active window, 545
Add a Logo (project), 507–512
add_blank_page() method, 419
add_break() method (Docx), 432
Add Bullets to Wiki Markup (project), 174
add_heading() method, 431
addingBoringcoinTransactions.py, 378
Adding Voice to Guess the Number (project), 574
add_paragraph() method, 430
add_picture() method, 433
add_run() method, 430
AES-256, 420
age attribute (PyTTSx3), 567
AI, 413–414
alert() function (PyMsgBox), 275
algebraic chess notation, 145
all_caps attribute (Docx), 428–429
all() method, 326
allMyCats1.py, 114
allMyCats2.py, 115
alpha transparency, 494
alternatingText.py, 173
alternation (|) operator, 191
ALTER TABLE query, 403, 404
Anaconda, 265
anchor, 225
and Boolean operator, 31
angle brackets (<>), 15, 20, 259, 301, 451
ANY_SINGLE constant, 212
ANYTHING_GREEDY constant, 212
ANYTHING_LAZY constant, 212
API (application programming interface), 297, 306, 359, 360
key, 297, 301
app, 258
append()
list method, 120, 142
PyPDF method, 416–417
append mode, 232
Apple, 259
application, 258
application programming interface. See API
apt command, 407, 528, 566, 578
archive file, 249
area attribute (PyAutoGUI), 552
arguments, 75, 130
ARIA (Accessible Rich Internet Applications), 325
arial.ttf, 515
arrays, 447
ASCII, 23
ASCII Art Fish Tank program, 271
ASCIIbetical order, 123
ASC keyword (SQLite), 397
as keyword, 233
assertion, 97–98
assert statement, 97–98
assigning, 87
assignment operator (=), 10, 130
assignment statement, 10
associative arrays, 447
asterisk (*)
glob, 227
multiplication operator, 6
regex, 197, 199
SQLite, 396
at_least() function (Humre), 211
at_least_group() function (Humre), 211
at_most() function (Humre), 211
at_most_group() function (Humre), 211
Atomic Consistent Isolated Durable (ACID) test, 393
Atom web feed format, 451
AT&T, 484
AttributeError, 64, 121, 540
attributes (HTML). See also names of individual attributes
href, 302
id, 302
overview, 302
attrs attribute (Beautiful Soup), 308
auditBoringcoin.py, 376
augmented assignment operators
augmented addition assignment operator (+=), 119
augmented division assignment operator (/=), 119
augmented modulus assignment operator (%=), 119
augmented multiplication assignment operator (*=), 119
augmented subtraction assignment operator (-=), 119
automateboringstuff3 package, 266
Auto Unsubscriber (project), 490
B
B:\ drive, 222
BACK_1 (Humre), 210
back() method (Selenium), 319
back reference, 203
backslash (\)
escape character, 190
line continuation character, 124
path separator (Windows), 218
BACK_SPACE constant (Selenium), 322
Back Up a Folder into a ZIP File (project), 252
backup.db, 402
backup() method (SQLite), 402, 406
bacon.txt, 232
banker’s rounding, 20
BarChart() function (Matplotlib), 354
bar() function (Matplotlib), 519
base-2 binary number system, 21
base-10 decimal number system, 21
basicConfig() function (logging module), 99
Batchfelder, Ned, 172
batch file, 258
%* (all arguments), 276
@ (hide command), 276
Beautiful Soup, 306–309
BeautifulSoup() function, 307
BEGIN query, 401
between() function (Humre), 211
between_group() function (Humre), 211
Bext package
bg() function, 270
clear() function, 271
fg() function, 270
get_key() function, 271
goto() function, 271
height() function, 271
hide() function, 271
show() function, 271
title() function, 271
width() function, 271
Beyond the Basic Stuff with Python, 258, 461
bg() function (Bext), 270
Big Book of Small Python Projects, The, 70, 154, 180, 271, 529
binary files, 229–230, 411
binary numbers, 21–23, 134, 172
binding, 87
birthdays.py, 141
bits, 22
bitwise or operator (|), 204
blank lines, 14, 15
Blank Row Inserter (project), 357
BLOB data type (SQLite), 389
blockchain, 376
block execution, 461
blocks of code, 34
body attribute (EZGmail), 482
bold attribute (Docx), 428–429
Boolean
and operator, 31
binary operators, 31
data type, 28
not operator, 32
or operator, 32
short-circuiting, 124
unary operators, 32
bool() function, 58
Boost Mobile, 484
borb package, 433
bottom attribute (PyAutoGUI), 552
bottomleft attribute (PyAutoGUI), 552
bottomright attribute (PyAutoGUI), 552
boundary, word, 201
bounding_box() method, 326
box attribute (PyAutoGUI), 552
box metaphor for variables, 10, 11
box tuple, 496
boxPrint.py, 96
braces ({})
with dictionaries, 139
with format() method, 150
with f-strings, 164
matching a number of qualifiers, 198
breakpoints, 106
break statement, 54
brew command, 528
browser
Chrome, 303
DB, 408
Developer Tools, 303
Edge, Microsoft, 303
Firefox, 303, 318
opening with web browser, 291
Tor, 290
Browser data type, 324
Browser Text Scraper (project), 536–538
brute-force password attack, 435
bs4 module, 307
buggyAddingProgram.py, 104
build folder (PyInstaller), 285
built-in functions, 63
bulletPointAdder.py, 174
By.CLASS_NAME constant, 320
By.CSS_SELECTOR constant, 320
By.ID constant, 320
By.LINK_TEXT constant, 320
By.NAME constant, 320
By.PARTIAL_LINK_TEXT constant, 320
By.TAG_NAME constant, 320
bytes, 22, 172, 296
bytes data type, 296, 456
C
C:\ drive, 218, 222
calcProd.py, 460
Calibri font, 348
call stack, 80–81
camelCase, 12
captcha (Completely Automated Public Turing test to tell Computers and Humans Apart), 555
capture_output parameter, 473
caret symbol (^)
matching beginning of string, 201
negative character classes, 193
Cascading Style Sheets. See CSS
case sensitivity, 12, 203, 218, 396, 485
Cat Vaccination Checker (project), 409–410
ccwd command, 279
ccwd.py, 279
cd command, 260
Cell data type, 334
cell phone provider
AT&T, 484
Boost Mobile, 484
Cricket, 484
Google Fi, 484
Metro PCS, 484
Republic Wireless, 484
Sprint, 484
T-Mobile, 484
U.S. Cellular, 484
Verizon, 484
Virgin Mobile, 484
Xfinity Mobile, 484
cells, in spreadsheet, 332, 363
census2010.py, 342
censuspopdata.xlsx, 338
center attribute (PyAutoGUI), 552
center() method, 171
centerx attribute (PyAutoGUI), 552
centery attribute (PyAutoGUI), 552
character classes
creating, 193
negative, 193
shorthand, 193
characterCount.py, 145
character styles, 427
chars() function (Humre), 211
chart, 354, 517
Chart data type (OpenPyXL), 354
ChatGPT (LLM), 414, 530
chdir() function, 221, 279
check() method (Playwright), 327
chessboard, 145–146, 147
Chess Dictionary Validator (project), 156
child elements (XML), 451
chmod command, 277, 278, 280, 281
choice() function (random module), 118, 133
chr() function, 172
Chrome browser, 303
chromium.launch() function, 324
circuits, 22
CLASS_NAME constant (Selenium), 320
clauses, 33
clear command, 272
clear() function (Bext), 271
clear() function (cls/clear command), 272
clear() method (Selenium), 320
click() function (PyAutoGUI), 544
click() method (Playwright), 326, 327
click() method (Selenium), 321
clipboard, 270
Clipboard Recorder (project), 281
cliprec.bat, 283
cliprec.command, 284
cliprec.desktop, 284
cliprec.py, 282
“closed, open” format, 61
close() method
File data type, 230, 232
Playwright module, 324
PyAutoGUI module, 555
shelve module, 234
sqlite3 module, 389
zipfile module, 251
cls command, 272
Cm() function, 433
code point (Unicode), 172
code style, 12
Coin Flip Streaks (project), 137
Collatz Sequence (project), 94
colon (:), 34, 468
color, 494
pixels, 494
RGBA value, 494
RGB value, 494
text, 270
Colorama package, 270
colormap variable (Pillow), 495
column attribute (OpenPyXL), 334
columnCount attribute, 371
column_dimensions attribute (OpenPyXL), 351
column_index_from_string() function, 336
columns, in Excel spreadsheets
converting letters and numbers, 336
setting width, 351
merging and unmerging, 352
Combine Select Pages from Many PDFs (project), 422
Comma Code (project), 136
comma-delimited, 111
command line arguments, 269, 472
command line interface (CLI), 259
command prompt, 259
commands, 258
names, 268
comma-separated values. See CSV
comments
overview, 14
multiline, 162
comparison operators, 29
compile() function (re module), 188
compiling Python programs, 285
CompletedProcess data type, 471
compressed files
creating ZIP files, 249
extracting ZIP files, 251
overview, 249
reading ZIP files, 250
compression type, 250
conditional expressions, 272
conditions, 33
confirm() function (PyMsgBox), 275, 561
connect() function (SQLite), 388
Connection data type, 388
console, 259
Console, Google Cloud, 360
constants, 133, 149
context manager, 233
Continue (debugger), 103
continue statement, 55
conventions, xxxii, 6, 12, 15, 219, 263, 388, 389, 399, 452
convertAddress() function (EZSheets), 368–369
converting, spreadsheet column letters and numbers, 336
converting data types, 17
Converting Spreadsheets to Other Formats (project), 381
coordinate attribute (OpenPyXL), 334
Coordinated Universal Time (UTC), 460
coordinate system, 495
coordinate tuple, 495
copy command, 268
Copy CSS Selector, 306
copy() function
copy module, 131
Pillow module, 500–501, 502
Pyperclipimg module, 516
Pyperclip module, 173, 175, 270
shutil module, 244
copy module
copy() function, 131
deepcopy() function, 131
copyTo() method (EZSheets), 365, 374
copytree() function (shutil module), 245
countdown() function (PyAutoGUI), 560
count() method, 326
country code, ISO 3166, 299
cp1252 encoding, 231
cp command, 268
cProfile.run() function, 461
CPU, 267, 467, 569
CPU, hogging, 282, 283
CREATE INDEX query, 399
create_sheet() method, 343
CREATE TABLE query, 389
Creating Custom Seating Cards (project), 525
creating PDFs from images, 533
credentials
creating, 360
Google API, 361
logging in, 362
revoking, 362
Cricket, 484
critical() function (logging module), 101
cron, 473
crop() method (Pillow), 499
cropped.png, 499, 500
cropping images, 499–500
CRUD operations, 392
CSS (Cascading Style Sheets)
overview, 301
selector, 306, 327
CSS_SELECTOR constant (Selenium), 320
CSV (comma-separated values)
delimiter, 442
header rows, 442, 443
line terminator, 442
overview, 438–444
csv module
DictReader() function, 442
DictWriter() function, 443
reader() function, 439
writer() function, 440
writerow() method, 440
ctime() function (time module), 460
current working directory (CWD), 220, 269
C:\Users folder, 222
Custom Invitations (project), 435
cwd() function, 221
D
Danjou, Julien, 234
Dash, Ubuntu Linux, 278
dashboard app, 274
database, in-memory, 406
DatabaseError, 388
databases
backing up, 402, 406
entry, 385
foreign key, 404
overview, 383
primary key, 385
relational, 385
row, 385
SQLite features, 387
vs. spreadsheets, 384
table, 385
data_only named parameter, 350
data serialization formats, 437
data type, 7
date arithmetic, 466
datetime module, 464–469
datetime() function, 335, 464
fromstimestamp(), 464
now() function, 464
timedelta() function, 465
day attribute (datetime module), 464
DB Browser app, 408
DBeaver Community app, 408
debug() function (logging module), 99
debugger
breakpoints, 106
Continue, 103
overview, 103
Step In, 103
Step Out, 104
Step Over, 103
Debugging Coin Toss (project), 108
decimal numbers, 21
decode() method (xml module), 456
decrypt() method (PyPDF), 421, 436
deduplicating, 75
deepcopy() function (copy module), 131
default application for file extension, 473
defining functions, 76
deflate compression algorithm, 250
def statement, 74
DELETE constant (Selenium), 322
DELETE FROM query, 392, 401
delete() method (EZSheets), 365–366
Deleting Unneeded Files (project), 255–256
delimiter (CSV), 442
del statement, 114, 122
demo.docx, 425, 426, 429
DESC keyword, 397
Developer Tools (Browser), 303
diamonds, flowchart, 28
dictionaries
checking if a key exists, 143
get() method, 144
items() method, 142
keys() method, 142
overview, 139
nested, 154
setdefault() method, 144, 341, 377
unordered, 140
values() method, 142
dictionary.txt, 435
DictReader() function, 442
DictWriter() function, 443
DIGIT constant (Humre), 210
dimensions3.xlsx, 351
dir command, 228, 260
directories, 218, 221
disable() function (logging module), 101
dishonestcapacity.py, 45
dist folder (PyInstaller), 285
Doctorow, Cory, 186
Document data type (Docx), 425
Document() function (Docx), 425, 430
Document Object Model (DOM), 453
docx module
add_break() method, 432
add_heading() method, 431
add_picture() method, 433
all_caps attribute, 428–429
bold attribute, 428–429
Cm() function, 433
Document() function, 425, 430
double_strike attribute, 428–429
emboss attribute, 428–429
imprint attribute, 428–429
Inches() function, 433
italic attribute, 428–429
outline attribute, 428–429
overview, 424
rtl attribute, 428–429
runs attribute, 426
shadow attribute, 428–429
small_caps attribute, 428–429
strike attribute, 428–429
style attribute, 427
text attribute, 425
underline attribute, 428–429
WD_BREAK.PAGE constant, 432
dollar sign ($), 201
domain name, URL, 299
dot (.)
current folder, 222
regex, 194
DOTALL constant (re module), 200
dot-dot (..) parent folder, 222
dot-star (.*), 199
doubleClick() function (PyAutoGUI), 544
double negatives, 32
DOUBLE_QUOTE constant (Humre), 210
double quotes ("), 160
double_strike attribute (Docx), 428–429
DOWN constant (Selenium), 322
downloadAllAttachments() function (EZGmail), 483
downloadAsCSV() method (EZSheets), 366
downloadAsExcel() method (EZSheets), 366
downloadAsHTML() method (EZSheets), 366
downloadAsODS() method (EZSheets), 366
downloadAsPDF() method (EZSheets), 366
downloadAsTSV() method (EZSheets), 366
downloadAttachment() function (EZGmail), 483
downloadFolder argument, 483
downloading
attachments, 483
files, 296
videos, 571–573
weather forecasts, 297
web comics, 312
web pages, 294
Downloading Google Forms Data (project), 380
download() method (yt-dlp), 571
Download XKCD Comics (project), 312
downloadXkcdComics.py, 313
drag() function (PyAutoGUI), 545
dragging, 545
dragTo() function (PyAutoGUI), 545
Draw() function (Pillow), 512, 514
drawing.png, 514
drives, 218, 225
DROP INDEX query, 399
dumps() function (json module), 450
E
echo command, 261, 578
Edge browser, Microsoft, 303
either() function (Humre), 211
Element data type (xml module), 453
Element() function (xml module), 456
elements
HTML, 301
XML, 451
ElementTree module, 453
elif statement, 37–38
ellipse() method (Pillow), 513, 514
else statement, 36–37
EMAIL_ADDRESS variable (EZGmail), 481
Email-Based Computer Control (project), 490
emails
downloading attachments, 483
reading, 481
searching, 482–483
sending, 480–481
emboss attribute (Docx), 428–429
encoding, 172
encoding named parameter, 231
encryption, 290
encrypt() method (PyPDF), 420–421
END constant (Selenium), 322
end named parameter, 79
ends_with() function (Humre), 211
endswith() method, 169
ENTER constant (Selenium), 322
entry (databases), 385
enumerate() function, 118, 370, 415
environment variables, 261
epoch, Unix, 460
equal to (==) operator, 29
error() function, 101
errors
AttributeError, 64, 121, 540
DatabaseError, 388
FileNotDecryptedError, 421
IndexError, 111
KeyError, 141, 144
ModuleNotFoundError, 267
NameError, 15, 114, 189
OperationalError, 389
SyntaxError, 7, 29
TypeError, 9, 16, 122, 220
UnboundLocalError, 87
escape characters
overview, 160
regular expressions, 190
ESCAPE constant (Selenium), 322
eSpeak, 566
evaluation, 19, 33
exactly() function (Humre), 211
exactly_group() function (Humre), 211
example3.xlsx, 438
example.db, 387
Excel
charts, 354
fonts, 348
formula, 345, 349, 350, 351
merging cells, 352
overview, 331
unmerging cells, 352
Excel-to-CSV Converter (project), 457
exceptions, 96
executable attribute (sys module), 267
execute() method (SQLite), 389
execution, 34
exist_ok named parameter, 244, 248
exists() method (pathlib module), 228
exitExample.py, 64
exit() function (sys module), 64
expand named parameter (Pillow), 504
exponent (**) operator, 6
extended ASCII, 231
Extensible Markup Language. See XML
extension, file, 225
extractall() method, 251
Extract Contact Information from Large Documents (project), 205
extractingpdfimages.py, 415
extract() method, 251
extractpdftext.py, 413
extract_text() method, 413
ezgmail module, 480–483
body attribute, 482
downloadAllAttachments() function, 483
downloadAttachment() function, 483
EMAIL_ADDRESS variable, 481
init() function, 480
messages attribute, 482
recent() function, 482
recipient attribute, 482
sender attribute, 482
send() function, 480–481
setup, 480
subject attribute, 482
summary() function, 481–482
timestamp attribute, 482
unread() function, 481–482
EZSheets
convertAddress() function, 368–369
downloadAsCSV() method, 366
downloadAsExcel() method, 366
downloadAsHTML() method, 366
downloadAsODS() method, 366
downloadAsPDF() method, 366
downloadAsTSV() method, 366
getColumnLetterOf() function, 368–369
getColumn() method, 369–370
getColumnNumberOf() function, 368–369
getRow() method, 369–370
getRows() method, 370–371
GmailThread data type, 481
listSpreadsheets() function, 364
overview, 359–360
Sheet() function, 367
Spreadsheet() function, 364
updateColumn() method, 369–370
updateRow() method, 369–370
updateRows() method, 370–371
F
f'' (f-string literal), 164
F1 constant (Selenium), 322
factorialLog.py, 99
failing fast, 98
FailSafeException (PyAutoGUI), 541
Fake Blockchain Cryptocurrency Scam (project), 375
False value, 28
falsey values, 58
Fantasia, 540
Fantasy Game Inventory (project), 156
fetchall() method (SQLite), 394–395
fg() function (Bext), 270
figure, 517
File data type, 230, 231
file editor
differences from interactive shell, 13
overview, 12
window, xl
file extension, 225, 260
filename, 217
FileNotDecryptedError, 421
fill() method (Playwright), 327
findall() method, 189, 192
find_element() method (Selenium), 306, 320
find_elements() method (Selenium), 320
Finding Mistakes in a Spreadsheet (project), 381
Firefox browser, 303, 318
Firefox() function, 318
firefox.launch() function, 323
first attribute (Playwright), 326
fiveTimes.py, 59
float() function, 16
floating-point numbers, 8, 23
flowchart, 28
flow control
blocks of code, 34
break statements, 54
conditions, 33
continue statements, 55
elif statements, 37–38
else statements, 36–37
for loops, 59–61
if statements, 35–36
while loops, 49–51
folders
home, 221
overview, 218, 221
parent, 222
root, 218
subfolders, 218
Font() function, 328
fonts (Excel), 348
foreign keys, 404
for loops
lists, 115
overview, 59–61
statement, 59
format_description attribute (Pillow), 498
format() method, 165
format specifier, 165, 207, 301, 366, 390, 437, 498, 569
forward() method (Selenium), 319
forward slash (/)
division operator, 6
path separator (macOS/Linux), 218
frankenstein_jpn.png, 533
frankenstein.png, 530, 531, 534
freeze pane (Excel), 353
freeze_panes attribute (OpenPyXL), 353
Friday the 13th Finder (project), 477
FROM keyword (SQLite), 394
from random import *, 64
fromstimestamp() (datetime module), 464
f-string, 164–165
functions. See also names of individual functions
calling, 14
defining, 76
def statement, 74
overview, 73
G
Gather Census Statistics (project), 338
Gauss, Carl Friedrich, 60
geckodriver, 319
Gemini (LLM), 530
gender attribute (PyTTSx3), 567
Generate Random Quiz Files (project), 235
getActiveWindow() function (PyAutoGUI), 552
getAllTitles() function (PyAutoGUI), 552
getAllWindowsAt() function (PyAutoGUI), 553
getAllWindows() function (PyAutoGUI), 553
getAllWindowsWithTitle() function (PyAutoGUI), 553
get_attribute() method (Selenium), 320, 326
get_by_alt_text() method (Playwright), 325
get_by_label() method, (Playwright) 325
get_by_placeholder() method (Playwright), 325
get_by_role() method (Playwright), 325
get_by_text() method (Playwright), 325
getcolor() function (Pillow), 494
getColumnLetterOf() function (EZSheets), 368–369
get_column_letters() function, 336
getColumn() method (EZSheets), 368–369
getColumnNumberOf() function (EZSheets), 368–369
getcwd() function, 221, 279
get() function (requests), 294, 298, 307
get_key() function (Bext), 271
get_languages() function (PyTesseract), 532
get() method (dictionaries), 144
getpixel() method (Pillow), 506
getProperty() method (PyTTSx3), 567
getroot() method (xml module), 453
getRow() method (EZSheets), 368–369
getRows() method (EZSheets), 370–371
gettext() method (Beautiful Soup), 308, 309
gigabyte (GB), 22, 45
global scope, 82
global statement, 85
globalStatement.py, 85
global variable, 82
glob() method, 227–228, 246
glob patterns, 227–228
Gmail, 360
GmailThread data type, 481
go_back() method (Playwright), 324
go_forward() method (Playwright), 324
Google Cloud, 360, 480
Google Drive API, 360
Google Fi, 484
Google Forms, 375
Google Sheets API, 359, 360
goto() function, 271
grammar, 7
graph, 517
Graphical User Interface (GUI), 259, 472, 540
greater than (>) operator, 29
greater than or equal to (>=) operator, 29
greedy matching, 199
grid() function (Matplotlib), 521
group_either() function (Humre), 211
group() function (Humre), 211
group() method (re module), 188, 190
groups, 189
groups() method (re module), 190
guessTheNumber.py, 65
guests.txt, 435
GUI (graphical user interface), 259, 472, 540
H
Harkins, Peter Bhat, 213
Hartley, Jonathan, 270
hash character (#), 14, 204
hash maps, 447
hash tables, 447
header rows (CSV), 442, 443
headless mode, 323
height attribute (Pillow), 498
height attribute (PyAutoGUI), 542, 552
height() function (Bext), 271
helloFunc.py, 73–74
helloFunc2.py, 75
hello.mp3, 272
hello.py, 13
hello.txt, 230, 231
hidden files, 279
hide() function, 271
hogging the CPU, 282
Homebrew (macOS package manager), 528
HOME constant (Selenium), 322
home folder, 221
horizontal_flip.png, 506
hotkey() function (PyAutoGUI), 559
hour attribute (datetime module), 464
href attribute (HTML), 302
HTML (HyperText Markup Language), 301
angle brackets, 301
attribute, 302
element, 301
overview, 301
tag, 301
Humre, 209
ANY_SINGLE constant, 212
ANYTHING_GREEDY constant, 212
ANYTHING_LAZY, constant 212
at_least() function, 211
at_least_group() function, 211
at_most() function, 211
at_most_group() function, 211
BACK_1 constant, 210
between() function, 211
between_group() function, 211
chars() function, 211
DIGIT constant, 210
DOUBLE_QUOTE constant, 210
either() function, 211
ends_with() function, 211
exactly() function, 211
exactly_group() function, 211
group_either() function, 211
group() function, 211
named_group() function, 211
NEWLINE constant, 210
nonchars() function, 211
NONDIGIT constant, 210
NONWHITESPACE constant, 210
NONWORD constant, 210
one_or_more() function, 211
one_or_more_group() function, 211
one_or_more_lazy() function, 211
one_or_more_lazy_group() function, 211
optional() function, 211
optional_group() function, 211
parse() function, 213
PERIOD constant, 210
QUOTE constant, 210
SOMETHING_GREEDY constant, 212
SOMETHING_LAZY constant, 212
starts_and_ends_with() function, 211
starts_with() function, 211
TAB constant, 210
WHITESPACE constant, 210
WORD constant, 210
zero_or_more() function, 211
zero_or_more_group() function, 211
zero_or_more_lazy() function, 211
zero_or_more_lazy_group() function, 211
HyperText Markup Language. See HTML
HyperText Transfer Protocol (HTTP), 289, 485
HyperText Transfer Protocol Secure (HTTPS), 289
I
I constant (re module), 203
id attribute (HTML), 302
ID constant (Selenium), 320
Identifying Photo Folders on the Hard Drive (project), 524
IEEE-754 standard, 23
IF NOT EXISTS, 389
if statement, 35–36
ImageColor.getcolor() function, 494
ImageColor module (Pillow), 494–495
Image data type (Pillow), 496, 548
Image data type (PyPDF), 416
ImageDraw data type, 512
ImageDraw.Draw() function, 512, 513
ImageDraw module (Pillow), 512
ImageFont data type (Pillow), 514, 515
ImageFont module (Pillow), 515
ImageFont.truetype() function, 515
Image.new() function, 499
ImageNotFoundException (PyAutoGUI), 550
Image Site Downloader (project), 330
image_to_string() function (PyTesseract), 533
immutable, 126
import as statement, 453, 517, 529
import statement, 63
imprint attribute (Docx), 428–429
Inches() function (Docx), 433
indentation, 34, 123–124
index
list, 110
negative, 111
SQLite, 399
string, 163
IndexError, 111
index() list method, 120
infinite loop, 54, 56, 282
info() function (logging module), 101
init() function (EZGmail), 480
init() function (PyTTSx3), 566
injection attack, 393
in keyword, 59
in-memory databases, 406
inner_html() method (Playwright), 326
inner_text() method (Playwright), 326
in operator, 116, 164
in place modification, 121, 127
input() function, 15, 267
Input Validation (project), 94
insert_blank_page() method, 419
INSERT INTO query, 392
insert() list method, 120–121
Inspect Element, 304
INT or (INTEGER) data type (SQLite), 389
integer (or int) data type, 8
integer division (//) operator, 6
Interactive Chessboard Simulator (project), 147
interactive shell
differences from file editor, 13
overview, xl, 4
prompt (>>>), xli
int() function, 16, 18
Invent Your Own Computer Games with Python, 148
is_absolute() method, 223
isActive attribute (PyAutoGUI), 555
isalnum() string method, 167, 168
isalpha() string method, 167, 168
is_checked() method (Playwright), 326
isdecimal() string method, 167, 168
is_dir() method, 228
is_displayed() method (Selenium), 320
is_enabled() method (Playwright), 326
is_enabled() method (Selenium), 320
is_encrypted attribute (PyPDF), 421
is_file() method, 228
islower() string method, 167, 168
isMaximized attribute (PyAutoGUI), 554
isMinimized attribute (PyAutoGUI), 554
ISO 3166 country code, 299
isolation_level named parameter, 388
isPhoneNumber.py, 186
is_selected() method (Selenium), 320
isspace() string method, 167, 168
istitle() string method, 167, 168
isupper() string method, 167, 168
is_visible() method (Playwright), 326
italic attribute (Docx), 428–429
items() dictionary method, 142
iter_content() method (Requests), 296
iterdir() method, 247
iter() method (xml module), 454, 455
J
JavaScript, 275, 318, 438
JavaScript Object Notation (JSON) 297, 386, 438, 448–451, 569
join() function (os.path module), 220
join() string method, 169
JSON (JavaScript Object Notation), 297, 386, 438, 448–451, 569
json.dumps() function, 450
json.loads() function, 298, 450, 488
K
key, API, 297
KeyboardInterrupt, 56, 90, 91, 134, 135, 282, 462, 463
KEYBOARD_KEYS constant (PyAutoGUI), 557
keyDown() function (PyAutoGUI), 558
KeyError, 141, 144
keys, dictionary, 139–140, 447, 452
Keys data type (Selenium)
BACK_SPACE constant, 322
DELETE constant, 322
DOWN constant, 322
END constant, 322
ENTER constant, 322
ESCAPE constant, 322
F1 constant, 322
HOME constant, 322
LEFT constant, 322
PAGE_DOWN constant, 322
PAGE_UP constant, 322
RETURN constant, 322
RIGHT constant, 322
TAB constant, 322
UP constant, 322
keys() dictionary method, 142
key=str.lower keyword argument, 123, 423
keyUp() function (PyAutoGUI), 558
key-value pair, 139–140, 144, 447, 452
kill() method (subprocess module), 472
kilobyte (KB), 22
L
lands (Blu-ray discs and DVDs), 22
lang named parameter (PyTesseract), 533
languages attribute (pyttsx), 567
Large Language Model (LLM), 414, 530–532
last attribute (Playwright), 326
latitude, 299
launchd, 473
lazy matching, 199
left attribute (PyAutoGUI), 552
LEFT constant (Selenium), 322
Legend data type (Matplotlib), 521
legend() function (Matplotlib), 521
len() function, 16, 113, 292
less than (<) operator, 29
less than or equal to (<=) operator, 29
LibreOffice, 332
license plate photo, 529
LIKE operator, 396
LIMIT keyword, 398
Line2D data type (Matplotlib), 517
line breaks (Word), 432
LineChart(), 355
line continuation character (\), 124
linegraph.png, 517
line() method (Pillow), 513, 514
linenum attribute, 440
line terminator (CSV), 442
lineterminator='\n\n' keyword argument, 441, 442
LINK_TEXT constant (Selenium), 320
Link Verification (project), 330
Linux
home folder, 222
path separator, 218
root folder, 218
Terminal, 4, 259
listdir() function (os module), 247
list() function, 128, 267
lists
concatenation, 113
data type, 110
indexes, 110
len() function, 113
list() function, 128, 267
nested, 154
slices, 112
tuple conversion, 128
listSpreadsheets() function, 364
List-to-Dictionary Loot Conversion (project), 157
literals, 30, 160, 161
littleKid.py, 43–44
ljust() string method, 171
LLaMA (LLM), 530
LLM (Large Language Model), 414, 530–532
load_model() function (Whisper), 568, 569
load_workbook() function, 333, 350
loads() function (json module), 298, 450, 488
localGlobalSameName.py, 84
local scope, 82
local variable, 82
locateAllOnScreen() function (PyAutoGUI), 550
locateOnScreen() function (PyAutoGUI), 550
location attribute (Selenium), 320
Locator data type (Playwright), 325, 326
locator() method, 325
logging levels, 101
logging module
basicConfig() function, 99
critical() function, 101
debug() function, 99
disable() function, 101
error() function, 101
info() function, 101
warning() function, 101
logout hotkey, 541
longitude, 299
Looking Busy (project), 563
loops
for, 59–61
while, 49–51
lower() string method, 166
ls command, 228, 260
lstrip() string method, 171
M
macOS
home folder, 222
path separator, 218
root folder, 218
Terminal, 4, 259
Mad Libs program, 240–241
magic8Ball2.py, 125
makedirs() function, 223
mappings, 447
Match data type (re module), 189
math operators, 6
Matplotlib, 517
matrixscreensaver.py, 132
max_column attribute, 335
maximize() method (PyAutoGUI), 555
maxResults named parameter, 482
max_row attribute, 335
McKenzie, Patrick, 195
Meal Ingredients Database (project), 410
megabyte (MB), 22
memory, 10, 21
merge_cells() method (OpenPyXL), 352
merge() method (PyPDF), 417
merge_page() method (PyPDF), 419
merging cells (Excel), 352
messages attribute (EZGmail), 482
metadata.json, 573
methods, 120
Metro PCS, 484
microseconds, 124, 464, 465, 469
Microsoft, 259, 331, 424, 493
Microsoft Edge browser, 303
Microsoft Speech API (SAPI5), 566
Microsoft SQL Server, 384
Microsoft Word, 424
midbottom attribute (PyAutoGUI), 552
middleClick() function (PyAutoGUI), 545
midleft attribute (PyAutoGUI), 552
midright attribute (PyAutoGUI), 552
midtop attribute (PyAutoGUI), 552
minimize() method (PyAutoGUI), 555
minute attribute (datetime module), 464
mkdir() method, 223, 244
MMS (multimedia messaging service), 484
ModuleNotFoundError, 267
modulus/remainder (%) operator, 6
month attribute (datetime module), 464
mouseDown() function (PyAutoGUI), 544
MouseInfo app, 547–548
mouseInfo() function (PyAutoGUI), 547
mouseUp() function (PyAutoGUI), 544
move() function (PyAutoGUI), 543
move() function (shutil module), 245
moveTo() function (PyAutoGUI), 542, 543
Mu code editor IDE
debugger, 103
installing, xxxix
starting, xl
multiline comments, 162
multiline string, 149, 161
multimedia messaging service (MMS), 484
multiple assignment trick, 117, 143
multiplication (*) operator, 6
Multiplication Table Maker (project), 356
mutable, 126, 129
myPets.py, 117
myProgramLog.txt, 100
MySQL, 384
myths about programming, xxxiv–xxxvi
N
name attribute (pyttsx), 567
NAME constant (Selenium), 320
named_group() function (Humre), 211
named parameters, 78–79
NameError, 15, 114, 189
namelist() method, 250
name tag metaphor for variables, 10, 129
NAPS2 app, 533–536
installing, 534
running from Python, 534
negative character class, 193
negative index, 111
nested dictionaries and lists, 154
new() function (Pillow), 499
NEWLINE constant (Humre), 210
new_name.txt, 245
new_page() method, 324
NFTs, 376
nonchars() function (Humre), 211
NONDIGIT constant (Humre), 210
None value, 39, 77–78, 449
non-greedy matching, 199
NONWHITESPACE constant (Humre), 210
NONWORD constant (Humre), 210
Norton Commander, 268
not Boolean operator, 32, 47
not equal to (!=) operator, 29
not in operator, 116, 164
NOT NULL (SQLite), 389, 391
now() function (datetime module), 464
NSSpeechSynthesizer, 566
ntfy service, 485
nth() method (Playwright), 326
NULL data type (SQLite), 389
null value (XML), 452
number, 8
O
OAuth, 361, 480
OCR (optical character recognition), 526, 529
odometer, 22
Office, 365, 332
one_or_more() function (Humre), 211
one_or_more_group() function (Humre), 211
one_or_more_lazy() function (Humre), 211
one_or_more_lazy_group() function (Humre), 211
Open All Search Results (project), 310
open command, 474
open() function (built-in), 230, 233, 413, 439, 440
open() function (shelve), 234
open() function (webbrowser), 291
open() method (Pillow), 496
openpyxl module
chart.BarChart() function, 354
chart.LineChart(), 355
chart.PieChart(), 355
chart.Reference() function, 354
chart.ScatterChart(), 355
chart.Series() function, 354
load_workbook() function, 333, 350
utils.column_index_from_string() function, 336
utils.get_column_letters() function, 336
OpenPyXL package, 332
OpenStreetMap, 291
OpenWeatherMap, 297, 299
OperationalError, 389
oppositeday.py, 44–45
optical character recognition (OCR), 526, 529
optional() function (Humre), 211
optional_group() function (Humre), 211
Oracle, 384
or Boolean operator, 32
ORDER BY clause, 397
order of operations, 6
ord() function, 172
origin, 495, 541
os module
chdir() function, 221, 279
getcwd() function, 221, 279
listdir() function, 247
makedirs() function, 223
path.exists() function, 229
path.isdir() function, 229
path.isfile() function, 229
path.join() function, 220
rmdir() function, 246
unlink() function, 246
walk() function, 247–249
outline attribute (Docx), 428–429
overlay, 419
P
page breaks (Word), 432
Page data type (Playwright), 324
Page data type (PyPDF), 413
PAGE_DOWN constant (Selenium), 322
pages attribute, 413
PAGE_UP constant (Selenium), 322
Paragraph data type, 425–426
parameters, 75
parent elements (XML), 451
parent folder, 222, 225
parentheses (()), 6, 14, 127
parents attribute, 225
parse() function (Humre), 213
parse() function (xml module), 453
parsing HTML, 304, 306
PARTIAL_LINK_TEXT constant (Selenium), 320
passingReference.py, 130
password() function, 275
PasswordType data type (PyPDF), 421
pasted.png, 501, 502
paste() function (Pyperclip), 173, 175, 270, 293
paste() function (Pyperclipimg), 516
paste() method (Pillow), 500–501, 503
path, URL, 299
Path.cwd() function, 221, 223
Path data type (pathlib module), 218, 572
PATH environment variable
editing, 261–262
geckodriver for Selenium, 319
overview, 261
Path() function, 218
Path.home() function, 221
pathlib module
overview, 218
Path data type, 218, 572
PosixPath data type, 219
WindowsPath data type, 219
Pattern data type, 188–189
pause command, 276
PAUSE variable (PyAutoGUI), 541
PDF (Portable Document Format), 411
extracting images, 415
extracting text, 412–413
owner password, 421
Password Breaker, 435
passwords, 420, 421
user password, 421
pdfkit package, 433
pdfminer module, 413
PDF Paranoia (project), 434
pdfplumber package, 433
PdfReader() function, 413, 415
pdfrw package, 433
PdfWriter() function, 416
PEP 8, 12
PERIOD constant (Humre), 210
pformat() function, 341
PieChart(), 355
pie() function (Matplotlib), 520
Pig Latin (project), 176
pigLat.py, 176
Pillow package, 494
ping command, 473
pip (pip installs packages), 264, 265
pipe character (|), 191, 205
pits (Blu-ray discs and DVDs), 22
pixel() function (PyAutoGUI), 549
pixelMatchesColor() function (PyAutoGUI), 549
pixels, 23, 494, 506
plaintext files, 229, 235, 301, 425, 437, 447, 448, 451
platform attribute, 267
playsound() function, 272
playsound3 package, 272
playwright module
chromium.launch() function, 324
firefox.launch() function, 323
overview, 323
webkit.launch() function, 324
plt module (Matplotlib), 517
bar() function, 519
grid() function, 521
legend() function, 521
pie() function, 520
plot() function, 517, 521
savefig() function, 517
scatter() function, 518
show() function, 517, 518, 519, 520, 521
title() function, 521
xlabel() function, 521
ylabel() function, 521
plus sign (+)
addition operator, 6
concatenation operator, 8, 113
match one or more, 197
point() method (Pillow), 512, 514
Point named tuple (PyAutoGUI), 543, 544, 552
poll() method (subprocess module), 471
polygon() method (Pillow), 513, 514
Popen() function (subprocess module), 471
Portable Document Format. See PDF
position() function (PyAutoGUI), 543, 544
POSIX, 219
PosixPath data type (pathlib module), 219
post() function (Requests), 486
PostgreSQL, 384
PowerShell, 259
pprint() function (pprint module), 396, 397, 403
pprint module
pformat() function, 341
pprint() function, 396, 397, 403
PRAGMA TABLE_INFO query, 391
PRAGMA query, 391, 405, 406
precedence, 6, 33
preprocessing images for OCR, 529
press() function (PyAutoGUI), 558
press() method (Playwright), 327
Prettified Stopwatch (project), 476–477
print debugging, 101
print() function, 14, 101, 267, 270
printRandom.py, 63
produceSales3.xlsx, 345
profiling code, 460
program
execution, 34
loading, 14
overview, 12
running, 13
saving, 14
project.docx, 217
prompt, xli, 4, 13, 259
prompt() function (PyMsgBox), 275
pub-sub notification services, 485
purpleImage.png, 499
push notifications
receiving, 487–489
sending, 485–486
transmitting metadata, 486–487
putpixel() method (Pillow), 506
putPixel.png, 506, 507
pwd command, 260, 279
PyAutoGUI, 540
PyAutoGUI, fail-safes, 541
pyautogui module
click() function, 544
countdown() function, 560
doubleClick() function, 544
drag() function, 545
dragTo() function, 545
FailSafeException, 541
getActiveWindow() function, 552
getAllTitles() function, 552
getAllWindowsAt() function, 553
getAllWindows() function, 553
getAllWindowsWithTitle() function, 553
hotkey() function, 559
ImageNotFoundException, 550
KEYBOARD_KEYS constant, 557
keyDown() function, 558
keyUp() function, 558
locateAllOnScreen() function, 550
locateOnScreen() function, 550
middleClick() function, 545
mouseDown() function, 544
mouseInfo() function, 547
mouseUp() function, 544
move() function, 543
moveTo() function, 542, 543
PAUSE variable, 541
pixel() function, 549
pixelMatchesColor() function, 549
position() function, 543, 544
press() function, 558
pyautogui.py, 540
rightClick() function, 544
screenshot() function, 548
scroll() function, 546, 547
size() function, 542
sleep() function, 560
useImageNotFoundException() function, 551
write() function, 556
PyCon, 172, 195
Pygame, 148
PyInstaller package, 285
pymsgbox module
alert() function, 275
confirm() function, 275
overview, 274
password() function, 275
prompt() function, 275
PyMuPDF package, 433
PyPDF package, 412, 415
pypdf.PdfReader() function, 413, 415
pypdf.PdfWriter() function, 416
pyperclipimg package
copy() function, 516
paste() function, 516
pyperclip module
copy() function, 173, 175, 270, 279
paste() function, 173, 175, 270, 293
PyPI, 265, 577
PyTesseract, 527
Python, xxxiv
Python-Docx package. See docx module
Python Package Index, 265, 577
Python Tutor website, 14
pyttsx3.init() function, 566
PyTTSx3 package, 566
Q
qualifiers (regex), 193
quantifiers (regex), 193, 195
queries (SQLite), 387
ALTER TABLE, 403, 404
BEGIN, 401
CREATE INDEX, 399
DELETE FROM, 392, 401
DROP INDEX, 399
INSERT INTO, 392
PRAGMA, 405, 406
PRAGMA TABLE_INFO, 391
SELECT, 391, 392, 394
UPDATE, 392, 400
query language, 384
query string (URL) 299
question mark (?)
optional match, 196
SQLite wildcard, 393
quit() method (Selenium), 319
quotas, Google Sheets, 379
QUOTE constant (Humre), 210
R
r'' (raw string literal), 161
raise_for_status() method, 295
raise statement, 96
randint() function (random module), 63, 66
random module
choice() function, 118, 133
randint() function, 63, 66
shuffle() function, 118
randomQuizGenerator.py, 236
range() function, 59, 62, 116
raw strings, 161
readCensusExcel.py, 339
reader() function (csv module), 439
Reading Text Fields with the Clipboard (project), 563
readlines() method (File data type), 231
read() method (File data type), 230
read mode, 231
read_text() method, 230
REAL data type (SQLite), 389
recent() function (EZGmail), 482
recipient attribute (EZGmail), 482
record (databases), 385
rectangle() method (Pillow), 513, 514
rectangles, flowchart, 28
Recursion_Chapter1.pdf, 413
Recursive Book of Recursion, The, 412
reference, 129–130, 131
Reference data type (OpenPyXL), 354
refresh() method (EZSheets), 365
refresh() method (Selenium), 319
regex. See regular expressions
Regex Search (project), 241
Regex Version of the strip() Method (project), 215
regular expression
groups, 189
overview, 186
parsing HTML, 304
qualifiers, 193
quantifiers, 193, 195
strings, 161
testers, 189
verbose mode, 204
relational databases, 385
relational operators, 29
relative path, 222
reload() method (Playwright), 324
remainder/modulous operator (%), 6
re module
compile() function, 188
DOTALL constant, 200
I constant, 203
Match data type, 189
Pattern data type, 188–189
VERBOSE constant, 204
remove() list method, 121
Remove the Header from CSV Files program, 444–447
render, 302
Renumbering Files (project), 256
ReportLab package, 433
Republic Wireless, 484
requests module
checking for errors, 294
downloading files with, 294
get() function, 294, 298, 307
post() function, 486
resize() method (Pillow), 503
resolution (screen), 542
Response data type (Requests), 294, 295, 298
restore() method (PyAutoGUI), 555
restyled.docx, 429
RETURN constant (Selenium), 322
return statement, 76–77, 80
return value, 76 –77
reverse() list method, 123
RGBA value, 494
RGB value, 494
right attribute (PyAutoGUI), 552
rightClick() function (PyAutoGUI), 544
RIGHT constant (Selenium), 322
rj.txt, 296
rjust() method, 170–171
rmdir() function (os module), 246
rmtree() function (shutil module), 246
RoboCop, 193, 203, 289, 435, 482, 483
robotic process automation (RPA), 540
Rock, Paper, Scissors, 67
rolling back transactions, SQLite, 401
Romeo and Juliet, 23, 294, 296
root element (XML), 451
root folder, 218
rotated180.png, 504
rotated270.png, 504
rotated6_expanded.png, 504, 505
rotated6.png, 504, 505
rotated90.png, 504
rotate() method (Pillow), 504
rotate() method (PyPDF), 418
round() function, 20, 46
rounding numbers, 20
row (databases), 385
row attribute (OpenPyXL), 334
rowCount attribute, 371
row_dimensions attribute (OpenPyXL), 351
rowid, 385
RPA (robotic process automation), 540
rpsGame.py, 67–68
RSS web feed format, 451
rstrip() string method, 171
rtl attribute (Docx), 428–429
runAndWait() method (PyTTSx3), 566
Run data type (Docx), 425–426
Run dialog, Windows, 276
run() function (cProfile module), 461
run() function (subprocess module), 471
runs attribute (Docx), 426
S
sameNameError.py, 86
sameNameLocalGlobal.py, 86
sampleChart3.xlsx, 354
sanitize() method (yt-dlp), 573
SAPI5 (Microsoft Speech API), 566
savefig() function (Matplotlib), 517
save() method (Docx), 430, 431
save() method (OpenPyXL), 343
save() method (Pillow), 498
save_to_file() method (PyTTSx3), 568
SAX (XML), 453
say() method (PyTTSx3), 566
ScatterChart(), 355
scatter() function (Matplotlib), 518
scheme, URL, 299
scopes (Google API), 361
scopes (variable), 82
Scott, Tom, 173, 290
screenshot() function (PyAutoGUI), 548
script, 258
scroll() function (PyAutoGUI), 546, 547
search() method, 188, 192
searchpypi.py, 310
second attribute (datetime module), 464
Selectively Copying (project), 255
SELECT keyword, 394
select() method, 306, 307–308
SELECT query, 391, 392, 394
Selenium package, 318
send2trash() function, 247
send2trash module, 247
sender attribute (EZGmail), 482
send() function (EZGmail), 480–481
send_keys() method (Selenium), 321
Series data type (OpenPyXL), 354
Serious Python, 234
set_checked() method, 327
setdefault() method, 144, 341, 377
set() method (xml module), 456
setProperty() method (PyTTSx3), 567
shadow attribute (Docx), 428–429
Shakespeare, William, 294
sheet, 332, 363
Sheet data type (EZSheets), 367
Sheet() method (EZSheets), 372–373
sheetnames attribute, 343
sheets attribute (EZSheets), 365
sheetTitles attribute (EZSheets), 365, 367, 373
shell, 259
shell script, 258
shelve module, 234
short-circuiting, 124
shorthand character class, 194
short message service (SMS), 484
show() function (Bext), 271
show() function (Matplotlib), 517, 518, 519, 520, 521
showmap.py, 291
show() method (Pillow), 496
shuffle() (random module), 118
shutil module, 244
copy() function, 244
copytree() function, 245
move() function, 245
rmtree() function, 246
Simple API for XML (SAX), 453
Simple Countdown (project), 474
simplecountdown.py, 474
Singing “99 Bottles of Beer” (project), 575
single quote ('), 8, 160
size attribute (Pillow), 498
size attribute (PyAutoGUI), 552
size attribute (Selenium), 320
size() function (PyAutoGUI), 542
Size named tuple (PyAutoGUI), 542, 552
sleep() function (PyAutoGUI), 560
sleep() function (time module), 89, 92, 135, 271, 274, 461
slice, 112, 163
slow_mo named parameter, 324
small_caps attribute (Docx), 428–429
Smith, Kurtwood, 289
SMS (short message service), 484
email gateways
disadvantages, 485
overview, 484–485
snake_case, 12
Snowstorm program, 273–274
SOMETHING_GREEDY constant (Humre), 212
SOMETHING_LAZY constant (Humre), 212
sonnet29.txt, 231
Sorcerer’s Apprentice, The, 540
sort() list method, 98, 122–123, 397, 422, 423
source (HTML), 302
source command, 264
spam.txt, 230
spike.py, 91
spiralDraw.py, 545
splitlines() method, 488
split() method, 170
Spotlight, 277
spreadsheet, 331, 363. See also workbook
spreadsheet app, 331
Spreadsheet data type (EZSheets), 364
Spreadsheet() function (EZSheets), 364
Sprint, 484
SQL (Structured Query Language), 384
SQLite, 384
apps
DB Browser, 408
DBeaver Community, 408
sqlite3.exe, 407
SQLite Studio, 408
comparison, 387
index, 399
injection attack, 393
overview, 384
rowid, 385
strict mode, 390
type affinity, 390
sqlite3.exe app, 407
sqlite3 module, 384
connect() function, 388
DatabaseError, 388
OperationalError, 389
sqlite_version variable, 390
sqlite_schema table, 391
SQLite Studio app, 408
square brackets ([]), 110, 112, 123
SRT (SubRip Subtitle), 570
stamp, 419
standard library, 63
standard output, 473
star character (*), 197
start command, 474
start() method (Playwright), 324
starts_and_ends_with() function (Humre), 211
starts_with() function (Humre), 211
startswith() string method, 169
st_atime attribute, 226
stat() method, 225
stat_result data type, 225
status_code attribute, 294
st_ctime attribute, 226
stdout attribute, 473
stem, 225
step argument for range(), 62, 335
Step In (debugger), 103
Step Out (debugger), 104
Step Over (debugger), 103
st_mtime attribute, 226
stop() method (Playwright), 324
strftime directives, 467–468
strftime() function (time module), 467–468
str() function, 16, 18
strict mode (SQLite), 390
strike attribute (Docx), 428–429
strings
concatenation, 8
copying to clipboard, 173
f-strings, 164
interpolation, 165
length, 16
literals, 160
methods, 166–171
multiline, 149, 161
overview, 7–8, 160
pasting from clipboard, 173
raw, 161
replication, 9
triple quotes, 162, 204
strip() string method, 171, 172
Strong Password Detection (project), 215
strptime() function (time module), 468–469
Structured Query Language (SQL), 384
st_size attribute, 226
style (Word), 425
style attribute (Docx), 427
styling paragraphs and runs (Word), 427
SubElement() function (xml module), 456
subelements (XML), 451
subfolders, 218
subject attribute (EZGmail), 482
sub() method (re module), 203
submit() method, 321
submit.png, 551
subprocess.Popen() function, 471, 472
subprocess.run() function, 470–471
SubRip Subtitle (SRT), 570
subtraction (-) operator, 6
sudo command, 407, 528, 566, 578
suffix, 225
summary() function (EZGmail), 481–482
Super Stopwatch (project), 462–464
suprocess module, 470
svelte.png, 503
SVG images, 451
Sweigart, Al, 363, 376
sweigartcats.db, 394–407, 409
sweigartcats-queries.txt, 407
SyntaxError, 7, 29
sys module
argv variable, 269, 292
executable attribute, 267
exit() function, 64
platform attribute, 267
version_info.major, 267
version_info.minor, 267
system Python, 264
T
TAB constant (Humre), 210
TAB constant (Selenium), 322
Table Printer (project), 181
tables (databases), 385, 391
tab-separated values (TSV), 441–442, 570
tag (HTML), 301
tag attribute (xml module), 454
Tag data type (Beautiful Soup), 308
tag_name attribute, 320
TAG_NAME constant (Selenium), 320
Task Scheduler, 473
terabyte (TB), 22, 45
terminal, 259, 270
terminating programs, 13, 64
ternary operators, 272
Tesseract, 527
tesseract.exe, 527
tess.get_languages() function (PyTesseract), 532
tess.image_to_string() function (PyTesseract), 533
text attribute (Docx), 425
text attribute (Requests), 294, 298, 307
text attribute (Selenium), 320
text attribute (xml module), 454
Text-based User Interface (TUI), 268
TEXT data type (SQLite), 389
text() method (Pillow), 514
text.png, 515, 516
text recognition, 526
text-to-speech (TTS), 566
third-party packages, 173, 209, 247, 270
tiled.png, 502, 503
Tile Maker (project), 524
timedelta data type (datetime module), 465
time() function (time module), 460
time module
ctime() function, 460
sleep() function, 89, 92, 135, 271, 274, 461
strftime() function, 467–468
strptime() function, 468–469
time() function, 460
Times New Roman, 348, 349
timestamp attribute (EZGmail), 482
title attribute (PyAutoGUI), 552
title() function (Bext), 271
title() function (Matplotlib), 521
T-Mobile, 484
TOML (Tom’s Obvious Markup Language), 447
top attribute (PyAutoGUI), 552
topleft attribute (PyAutoGUI), 552
topright attribute (PyAutoGUI), 552
Tor anonymization network, 290
Tor Browser, 290
tostring() function (xml module), 456
total_seconds() method, 465
transactions (databases)
ACID compliance, 393
overview, 393
rolling back, 401
transcribe() method (Whisper), 568, 569
transparency, alpha, 494
transparentImage.png, 499
transpose() method (Pillow), 505, 506
Trash folder, Google Drive, 366
triple quotes ('''), 162, 204
TrueType fonts, 515
truetype() function (Pillow), 515
True value, 28
truth table, 31
truthy values, 58
TSV (tab-separated values), 441–442, 570
TTS (text-to-speech), 566
TUI (Text-based User Interface), 268
tuple
data type, 127
unpacking, 117
tuple() function, 128, 542
Twilio, 485
two’s complement, 23
type affinity, 390
TypeError, 9, 16, 122, 220
type() function, 19–20
U
Ubuntu Linux Dash, 278
Umbrella Reminder (project), 490
unbalanced parentheses, 191
UnboundLocalError, 87
uncheck() method (Playwright), 327
underline attribute (Docx), 428–429
underscore (_), 11, 12, 194
unhashable, 143
Unicode code point, 172
Uniform Resource Locator. See URL
Unix
epoch, 460
philosophy, 272
POSIX standard, 219
unlink() function (os module), 246
unmerge_cells() method (OpenPyXL), 352
unmerging cells (Excel), 352
unread() function (EZGmail), 481–482
unterminated string literal, 8
UP constant (Selenium), 322
Update a Spreadsheet (project), 344–347
updateColumn() method (EZSheets), 368–369
updatedProduceSales3.xlsx, 347
updateProduce.py, 346
UPDATE query, 392, 400
updateRow() method (EZSheets), 368–369
updateRows() method (EZSheets), 370–371
upper() method, 166
URL (Uniform Resource Locator)
domain name, 299
overview, 290, 299, 310
path, 299
query string, 299
scheme, 299
U.S. Cellular, 484
useImageNotFoundException() function (PyAutoGUI), 551
UTC (Coordinated Universal Time), 460
UTF-8 encoding, 23, 172, 173
V
validateInput.py, 168
value attribute (OpenPyXL), 334
values (key-value pairs), 139–140, 447, 452
values() dictionary method, 142
vampire.py, 39–40
vampire2.py, 41–42
variables
camelCase, 12
initialization, 10
metaphors, 10, 11, 129
names, 11
overview, 12
overwriting, 10–11
snake_case, 12
venv module, 263
VERBOSE constant (re module), 204
verbose mode, 204
Verizon, 484
version_info.major, 267
version_info.minor, 267
vertical_flip.png, 506
View Page Source, 302
View Source, 302
Virgin Mobile, 484
virtual environments, 263
virtual private network (VPN), 290
Voice data type, 567
voltage, 22
VTT (Web Video Text Tracks), 570
W
wait() method, 471
WAL (Write-Ahead Logging), 388
walk() function, 247–249
warning() function, 101
watermark.pdf, 419
WD_BREAK.PAGE, 432
weather API, 297
web3, 376
web app, 258
webbrowser module, 291
WebDriver data type, 318, 319
webdriver.Firefox() function, 318
WebElement data type, 319–320
web feed formats
Atom, 451
RSS, 451
webkit.launch() function, 324
Web Video Text Tracks (VTT), 570
WHERE clause, 394, 400, 401
where command, 263
which command, 262
while loops, 49–51, 61
while statement, 49
whisper.load_model() function, 568, 569
Whisper models
'base', 569
'large-v3', 569
'medium', 569
'small', 569
'tiny', 569
Whisper package, 568
whitespace, 6, 170, 171, 449, 452
WHITESPACE constant (Humre), 210
width attribute (Pillow), 498
width attribute (PyAutoGUI), 542, 552
width() function (Bext), 271
Willison, Simon, xxxvii
Win32Window data type (PyAutoGUI), 552
Window data type (PyAutoGUI), 552
Windows, Microsoft
Command Prompt, 4, 259
home folder, 222
path separator, 218
PowerShell, 259
root folder, 218
Terminal, 259
WindowsPath data type, 219
with statement, 233
word boundary, 201
WORD constant (Humre), 210
workbook, 332
Workbook data type, 333
Workbook() function, 343
worksheet, 332
Worksheet data type, 334
Write Ahead-Logging (WAL), 388
write binary mode, 296
writeFormula3.xlsx, 350
write() function (PyAutoGUI), 556
write() method (File data type), 230, 232, 413
write() method (ZipFile), 250
write mode, 232
writer() function (csv module), 440
writerow() method, 440, 442
write_text() method, 230
Writing a Game-Playing Bot (project), 563
X
x attribute (PyAutoGUI), 544
x-coordinate, 495, 496
Xfinity Mobile, 484
xlabel() function (Matplotlib), 521
XML (Extensible Markup Language), 297, 438
elements, 451
child, 451
parent, 451
root, 451
subelement, 451
overview, 297
tag attribute, 454
text attribute, 454
xml.dom module, 453
xml.etree.ElementTree module, 453
xml.sax module, 453
XPath, 306, 327, 455
Y
YAML, 447
y attribute (PyAutoGUI), 544
y-coordinate, 495, 496
year attribute (datetime module), 464
ylabel() function (Matplotlib), 521
yourName.py, 52
yourName2.py, 54
yourScript.bat, 277
yourScript.command, 277
yourScript.desktop, 278
yourScript.py, 259, 267, 269, 276, 285
YoutubeDL() function (yt-dlp), 571
YouTube Transcriber (project), 575
yt_dlp module, 571
yt-dlp package, 571
yt_dlp.YoutubeDL() function, 571
Z
zero_or_more() function (Humre), 211
zero_or_more_group() function (Humre), 211
zero_or_more_lazy() function (Humre), 211
zero_or_more_lazy_group() function (Humre), 211
zigzag.py, 89
ZIP_DEFLATED attribute, 250
ZIP file, 249
ZipFile data type, 249, 250
ZipFile() function, 250
zipfile module, 249
zipfile.ZIP_DEFLATED attribute, 250
zipfile.ZipFile() function, 250
ZipInfo data type, 251
Zira voice, 567
Zona, Carina C., 195
zophie.jpg, 498
zophie.png, 496, 498, 516
![obrazek](images/000000.jpg)
A flow chart showing how to evaluate the mathematical expression “5 minus 1 in parentheses, multiplied by the result of dividing seven plus one and three minus one.” First, five minus one reduces to four. Next, seven plus one reduces to eight. Then, three minus one reduces to two. After that, eight divided by two reduces to four. Finally, four times four produces the solution, sixteen.
Return to text
A diagram showing how an expression passed to the print function, “You will be ‘ + str(int(myage) + 1) + ‘ in a year,’ evaluates to its final value. First, “my age” is replaced by the string “4”. Then, “int” disappears, and the string “4” is replaced by the integer 4. Next, 4 + 1 evaluates to 5. After that, “str” disappears, and the integer “5” becomes the string “5”. Finally, the strings “You will be” and “5” and “in a year” are added together. The final result is the string “You will be 5 in a year.”
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the question “Is raining?” This question leads to two arrows, one labeled “yes” and one labeled “no.” The “no” branch leads to a box labeled “Go outside,” where a final arrow leads to a box labeled “End.” The “yes” branch leads to the question “Have umbrella?” which branches once again into a “yes” and a “no” arrow. The “yes” arrow leads to the “Go outside” box. The “no” arrow leads to a box labeled “Wait a while,” which leads to the question labeled “Is raining?” The “yes” arrow leads back to the “Wait a while” box. The “no” arrow leads to the “Go outside” box.
Return to text
A diagram evaluating the expression “four is less than five” in parentheses and “five is less than six” in parentheses. First, “four is less than five” reduces to “True.” Next, “five is less than six” reduces to True. Finally, “True and True” reduces to the final value, True.
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the box “name equals Alice,” which leads to the decision point “name equals Alice.” A “true” branch leads to the box “print(‘Hi,Alice.’)”, which leads to “End.” A “false” branch leads directly to “End.”
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the box “name equals Alice,” which leads to the decision point “name equals Alice.” A “true” branch leads to the box “print(‘Hi,Alice.’)”, which leads to “End.” A “false” branch leads to the box “print(‘Hello, stranger.’),” which leads to “End.”
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the box “name equals Alice,” which leads to a box labeled “age equals 15.” This box leads to the decision point “name equals Alice.” A “true” branch leads to the box “print(‘Hi, Alice.’)”, which leads to “End.” A “false” branch leads to the decision point “age is less than 12.”  A “true” branch leads to the box“print(‘You are not Alice, kiddo.’),” which leads to “End.” A “false” branch leads directly to “End.”
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the decision point “name equals Alice.” A “true” arrow leads to the box “print(‘Hi, Alice.’),” which leads to End. A “false” arrow leads to the decision point “age is less than 12.” From this decision point, a “true” arrow leads to the box “print(‘You are not Alice, Kiddo.’),” which leads to End. A false arrow leads to the decision point “age is greater than 2000.” From this decision point, a “true” arrow leads to the box “print(‘Unlike you, Alice is not an undead, immortal vampire.’), which leads to End. A “false’ arrow leads to the decision point “age is greater than 100.” From this decision point, a True arrow leads to the box “print(‘You are not Alice, grannie.’),” which leads to End. A False arrow leads directly to End.
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the decision point “name equals Alice.” A “true” arrow leads to the box “print(‘Hi, Alice.’),” which leads to End. A “false” arrow leads to the decision point “age is less than 12.” From this decision point, a “true” arrow leads to the box “print(‘You are not Alice, kiddo.’),” which leads to End. A false arrow leads to the decision point “age is greater than 100.” From this decision point, a True arrow leads to the box “print(‘You are not Alice, grannie.’),” which leads to End. A false arrow leads to the decision point “age is greater than 2000.” From this decision point, a “true” arrow leads to the box “print(‘Unlike you, Alice is not an undead, immortal vampire.’), which leads to End. A False arrow leads directly to End.
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the decision point “name equals Alice.” A “true” arrow leads to the box “print(‘Hi, Alice.’),” which leads to End. A “false” arrow leads to the decision point “age is less than 12.” From this decision point, a “true” arrow leads to the box “print(‘You are not Alice, kiddo.’),” which leads to End. A false arrow leads to the box “print(‘You are neither Alice nor a little kid.”),” which leads to End.
Return to text
A diagram showing the evaluation of a Python expression assigned to the variable “real_capacity.” The expression begins “str(round(advertised_capacity multiplied by discrepancy, 2)).” First, “advertised_capacity” evaluates to 10 and “discrepancy” evaluates to “0.9094947017729282.” Next, “round(10 multiplied by 0.9094947017729282, 2)” evaluates to “round(9.094947017729282, 2).” After that, the expression reduces to “str(9.09),” leading to the final value, the string “9.09”.
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the decision point “spam is less than 5.” A True arrow leads to the box “print(‘Hello, world.’), which leads to the box “spam equals spam plus 1,” which leads to End. A False arrow leads directly to end.
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the decision point “spam is less than 5.” A True arrow leads to the box “print(‘Hello, world.’), which leads to the box “spam equals spam plus 1,” which leads to back to the decision point “spam is less than 5.” A False arrow leads directly to end.
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the decision point “name does not equal ‘your name’.” A True arrow leads to the box “print(‘Please type your name.’),” which leads to the box “name equals input(),” which leads to back to the decision point “name does not equal ‘your name’.” A False arrow leads to the box “print(‘Thank you!’)”, which leads to end.
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the decision point “True.” From there, a crossed-out “False” branch leads to the box “print(Thank You!),” which leads to End, while a True arrow leads to the box “print(‘Please type your name.’),” which leads to the box “name equals input(),” which leads to the decision point “name is equal to ‘your name’.” From here, a True arrow leads to a box labeled “break,” which leads to “print(Thank You!),” which leads to End. A False arrow leads back to the first decision point in the flowchart, “True.”
Return to text
A flowchart that begins with a box labeled “Start.” An arrow leads to the decision point “True.” From there, a crossed-out “False” branch leads to the box “print(‘Access granted.’), which leads to End, while a True arrow leads to the box “print(‘Who are you?’),” which leads to the box “name equals input(),” which leads to the decision point “name is not equal to ‘Joe’.” From here, a True arrow leads to a box labeled “continue,” which leads back to the first decision point in the flowchart, “True.” A False arrow leads to the box “print(‘Hello, Joe. What is the password? (It is a fish.)’),” which leads to the box “password equals input(),” which leads to the decision point “password is equal to ‘swordfish.’” From there, a false arrow leads back to the original decision point, True, while a True arrow leads to a box labeled “break,” which leads to “print(‘Access granted.’), which leads to End.
Return to text
A flowchart that begins with a box labeled “Start.” An arrows leads to a box labeled “print(‘Hello’),” which leads to the decision point “for I in range (5).” From there, an arrow labeled “looping” leads to the box “print(‘On this iteration, I is set to ‘ + str(i)),” which leads back to the previous decision point, “for I in range (5).” At that decision point, another arrow, labeled “Done looping,” leads to End.
Return to text
The evolution of a stack of names, from left to right. The stack begins empty, then contains Alice, then contains Bob on top of Alice, then contains Carol on top of Bob on top of Alice, then contains Bob on top of Alice, then contains Alice, then contains David on top of Alice, then contains Alice, then is empty.
Return to text
The evolution of a stack of function calls, from left to right. The stack begins empty, then contains a(), then contains b() on top of a(), then contains c() on top of b() on top of a(), then contains b() on top of a(), then contains a(), then contains d() on top of a(), then contains a(), then is empty.
Return to text
A screenshot of the Mu interface. On the left side is a Python program with the first line highlighted, “print(‘Enter the first number to add:’).” On the right side are the lists “Name” and “Value” populated with the names and values of variables. At the bottom of the screen is the message ‘Running in debug mode. Use the Stop, Continue, and Step toolbar buttons to debug the script.”
Return to text
A screenshot of the Mu interface. On the left side is a Python program with the second line highlighted, “first = input()”. On the right side are the lists “Name” and “Value” populated with the names and values of variables.
Return to text
A screenshot of the Mu interface. On the left side is a Python program with the last line highlighted, “print(‘The sum is ‘ + first + second + third)”. On the right side are the lists “Name” and “Value” populated with the names and values of variables.
Return to text
A diagram showing how each item in the list “spam equals “cat”, “bat”, “rat”, “elephant”, corresponds to an index. “Cat” corresponds to the index “spam 0,” “bat” corresponds to the index “spam 1,” “rat corresponds to the index “spam 2,” and “elephant corresponds to the index “spam 3.”
Return to text
First, the Python assignment statement “spam equals 42” is represented as the value “42” with the tag “spam” attached to it. Second, the Python assignment statement “eggs equals spam” is represented as the value “42” with two tags, labeled “spam” and “eggs,” attached to it. Third, the Python assignment statement “spam equals 99” is represented as two values; “42” has the tag “eggs” attached to it, and “99” has the tag “spam” attached to it.
Return to text
First, the Python assignment statement “spam equals 42” is represented as the value “[0, 1, 2, 3]” with the tag “spam” attached to it. Second, the Python assignment statement “eggs equals spam” is represented as the value “[0, 1, 2, 3]” with two tags, labeled “spam” and “eggs,” attached to it. Third, the Python assignment statement “eggs[1] = ‘Hello’” is represented as the value “[0, ‘Hello’, 2, 3]” with two tags, “eggs” and “spam”, attached to it.
Return to text
A diagram showing the evaluation of the value of a Path object. Path(‘spam’)/bacon’ becomes WindowsPath(‘spam/bacon’)/‘eggs’. This then becomes WindowsPath(‘spam/bacon/eggs’) /‘ham’. The final value is WindowsPath(‘spam/bacon/eggs/ham’).
Return to text
A diagram showing nested folders and files, accompanied by the relative and absolute paths of the folder or file at each level in the directory. The first folder is “C:\”, its relative path is “..\”, and its absolute path is “C:\”. Within this folder is a “bacon” folder. Its relative path is “.\” and its absolute path is “C:\bacon”. Within bacon is a “fizz” folder. Its relative path is “.\fizz” and its absolute path is “C:\bacon\fizz”. Within fizz is a file, “spam.txt.” Its relative path is .\fizz\spam.txt” and its absolute path is “C:\bacon\fizz\spam.txt.” The “bacon” folder also has a “spam.txt” file. Its relative path is “.\spam.txt” and its absolute path is “C:\bacon\fizz\spam.txt”. The “C:\” folder contains another folder, “eggs.” Its relative path is “..\eggs” and its absolute path is “C:\eggs\spam.txt”. Eggs contains a file, “spam.txt:. Its relative path is “..\eggs\spam.txt” and its absolute path is “C:\eggs\spam.txt”. Finally, the “C:\” folder directly contains its own “spam.txt” file. Its relative path is “..\spam.txt” and its absolute oath is “C:\spam.txt”.
Return to text
A diagram of a filepath on Windows and macOS showing the anchor, parent, name, drive, stem, and suffix. In the windows path “C:\Users\Al\spam.txt”, the drive is “C:”, the anchor is “C:\”, the parent is “\Users\Al\”, the name is “spam.txt”, the stem is “spam,” and the suffix is “.txt”. In the macOS filepath “/home/al/spam.txt”, the anchor is “/“, the parent is “home/al/“, the name is “spam.txt”, the stem is “spam”, and the suffix is “.txt”.
Return to text
A Word document containing several rows of text in various fonts. The first row uses a cursive font and says “It would be a pleasure to have the company of”. The second row uses a bold, sans-serif font and says “RoboCop”. The third row uses the same cursive font as the first row and says “at 11010 Memory Lane on the Evening of”. The fourth row uses sans-serif font and says “April 1st”. The final line contains the cursive font once again and says “at 7 o’clock”.
Return to text
![obrazek](/images/cover-automate3-thumb.webp)
![obrazek](/images/cover-bigbookpython-thumb.webp)
![obrazek](/images/cover-beyond-thumb.webp)
![obrazek](/images/cover-invent4th-thumb.webp)
![obrazek](/images/cover-crackingcodes-thumb.webp)