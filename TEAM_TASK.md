# Team Project Task

## Objective and Requirements
- Automate each related task from TASKS.md file (API mock tests, DB tests, Selenium tests)
- ✅ One related task category (API mock tests, DB tests, Selenium tests) should be associated to one person in your team
- Person associated to the category should add tests and make them work from docker container ONLY
- ✅ Team should organise project and use one (chosen by team) python package manager to deal with dependencies during development and during tests container running (default one is `poetry`)
- ☑️ Team should add tests logging into file (no strict requirements here) and may use any logging library team decide to use (recommended `logging`)
- Team should organise tests data into yaml, json and/or env files and utilize them during tests run (recommended yaml files and `pyyaml` library)
- ✅ Team should use `pytest` as tests runner and base framework
- ☑️ Team should add and organise their helper classes and methods inside the specified local python package (recommended and default is `tests_lib`)
- Helper classes and methods shouldn't have hardcoded data, but it could have hardcoded paths to files where tests data is stored
- Helper classes should have AT LEAST 1 custom base class and it should be inherited and used by some child helper class
- Helper files should follow OOP principles and have NO MORE than 1 class in each file implemented
- ☑️ Each tests category should have own sub-directory under `tests` directory to store tests
- Try to follow SOLID, KISS and YAGNI principles during your code development as much as you can (not strict requirement, but highly recommended)
- Each team project repo should have master or main branch
- ☑️ Each code change should be processed through pull request (PR) from your custom branch to the master branch
- ☑️ Each PR should be approved by all team members before merge
- Teammates are allowed to comment and advice during PR review. It won't affect your team or personal scores, but it's highly recommended to do to enhance general project code quality
- If you have comment that is just minor suggestion for PR author and is not critical to implement - mark it as NIT (Non-Important Thing)
- PR author can decide to implement or not implement NIT comments
- If author decided your not NIT marked comment is NIT in fact and both can't agree - the last word to decide has your 3d teammate or if no 3d teammate - one of mentors
- If PR has all non-NIT comments addressed and agreed - PR should be approved by teammates and merged
- ☑️ Tests container should be started by one command and run all categories of tests your team has implemented.
- Only working and runnable tests inside docker container will be checked by mentor.
- HTTPS requests in API tests category is optional requirement. ) Team can use HTTP, it's acceptable

## Tasks

All tests tasks are described previously in TASKS.md file

> [!IMPORTANT]  
> Create new fork of this repository and provide a link to it when you are ready to deliver. If you already have a fork - use it to complete all tasks.

### Symbols of progress in the project

This designation was introduced for our project to help us understand which points we have already completed and which we are still working on.

- ❌ Not done
- ✅ Done
- ☑️ In progress


