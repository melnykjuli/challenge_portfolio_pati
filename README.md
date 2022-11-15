# Task 1: software configuration

## Subtask 1: Why did I choose to participate in the Dare IT Challenge?

Hi there!
My name is Yuliia, and I'm excited to take part in the DareIT Challenge to plan and hasten my learning.

I'm most excited about the challenge's methodical approach to studying new topics and boosting practical expertise. For me, it's also very important to have the chance to participate in a course that contains practice tests that are as close to tasks on real projects.


# TASK 2: selectors

## Title_Scouts Panel

```
//div//h5
//*[text()='Scouts Panel']
//*[contains(text(),"Scouts Panel")]
```

## Login 

```
//*[@id="login-label"]
//*[text()="Login"]
//label[@for='login']
```

## Login Input

```
//input[@name="login"]
//input[@id="login"]
//input[@type='text' and @name='login']
```

## Password Input

```
//input[@type='password']
//*[@type="password"]
//input[@id='password']
```

## Remind password

```
//a[text()='Remind password']
//*[text()='Remind password' and @tabindex='-1']
```

## Language

```
//*[@tabindex='0' and @role='button']
//*[@role="listbox"]
```

## Sign In Button

```
//*[contains(text(),"Sign in")]
//span["MuiButton-label"]
//span["MuiTouchRipple-root"]
```

## Subtask 3: Created dashboard.py file

Added locators for "dashboard" page

## Subtask 4: Created add_match.py

Added locators for "Add match" page

# TASK 3: First automatic test, asserts

Added task 3 with subtasks 1-5