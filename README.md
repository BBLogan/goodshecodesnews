Bex Logan - She Codes News Project

## About this project
Well this news story website certainly has taught me a lot - even concepts not in the teaching materials like how branch multiple times, how to merge, how to not loose your head and oh yeah building a responsive news website. Please note

## How to run the code
The below is set out for PC users - Mac ppl pls convert the terminal inputs

Step 1 - Clone the repository - Make sure you clone the repo into the right place
- terminal input01: `git clone <https://wwww.theurlofthisrepo.git>`
- terminal input02: `cd <to your folder name where you stored the repo>`

Step 2 - Create your Virtual environment - terminal input: `python -m venv venv`

Step 3 - Activate your Virtual environment (venv) - terminal input: `. venv/Scripts/activate`
- to turn on your VE for MS Surfaces you need to use: `source ./venv/Scripts/activate` to turn it on each time

Step 4 - Migrate the database - terminal input: `python manage.py migrate`

Step 5 - Open the repo - terminal input: `code .`

Step 6 - Run the server - terminal input: `python manage.py runserver`

Step 6 - Create a user account or log in and enjoy looking around News Cha Cha Cha

Step 7 - User Account details provided below Additional Features

## Database schema
My ERD - project_images\dbschema.png

## Project features
- Order stories by date
Stories order in date time chronology with no midnight - project_images\storiesindatetimeorder-nomidnight.png

- Styled "new story" form
Writing a new story - project_images\writenewstoryform01.png

- Story images
Static images - she_codes_news\news\static\news\images
Story images front page - project_images\frontpage-loggedout01.png

- Login / logout
logged in view navigation - project_images\loggedinnavigation.png
logged out view navigation - project_images\loggedoutnavigation.png

- "Account view" page
Loggedin Author Account View - project_images\myprofileview(loggedinauthor)01.png

- "Create Account" page
Create a new account form - project_images\createaccount01.png

- View stories by author
{description of image} {./relative_path_to_image_file}

- "Login" button only visible when no user is logged in / "Logout" button only visible when a user is logged in
Logged in view inside story update and delete buttons - project_images\storyviewloggedin02-update&delete.png
Logged out view inside story - project_images\storyviewloggedout01.png

- "Create Story" functionality only available when user is logged in
Create a new story image - logged in view - project_images\writenewstoryform01.png

## Additional Features
Please note no additional features are currently with this project (as of 23/12/2023). Future revisions of the project may have the below. The list is kept as a reminder

- [] Add categories to the stories and allow the user to search for stories by category
{description of image} {./relative_path_to_image_file}

- [] Add the ability to update and delete stories (consider permissions - who should be allowed to update &/ delete stories)
{description of image} {./relative_path_to_image_file}

- [] Add the ability to "favourite" stories and see a page with your favourite stories
{description of image} {./relative_path_to_image_file}

- [] Our form for creating stories requires you to add the publication date - update this to automatically save the publication date as the day the story was first published (maybe you could then add a field to show when the story was updated)
{description of image} {./relative_path_to_image_file}

- [] Gracefully handle the error wherre someone tries to create a new story when they're no logged in
{description of image} {./relative_path_to_image_file}

## Test Accounts
UN: samsamsam - PW: SamsYourMan01
UN: BBLogan02 - PW: Farts Farts Farts01
UN: bblogan1983 - PW: YnQkdzsyeY_Ji!4 (PW not used on anyother site)
