# Accuknox Django Trainee Assignment

---

# Project Overview

The assignment consists of two parts:

1. Investigating the behavior of Django Signals.
2. Implementing a custom iterable Rectangle class in Python.

The project has been implemented as a Django application as requested in the assignment instructions.

---

# Objectives

The Django Signals section aims to experimentally verify the following:

## Question 1

Are Django signals executed synchronously or asynchronously by default?

## Question 2

Do Django signals execute in the same thread as the caller?

## Question 3

Do Django signals execute in the same database transaction as the caller?

Additionally, a custom Python Rectangle class has been implemented which supports iteration.


---

# Django Signals

Django signals provide a mechanism for allowing certain senders to notify a set of receivers that some action has taken place.

For example:

* Saving a model
* Deleting a model
* User login
* User logout

This project uses the `post_save` signal.

---

# Question 1

## Are Django signals synchronous by default?

### Conclusion

Yes.

Django signals execute synchronously by default.

### Logic

A deliberate delay is introduced inside the signal using:

```python
time.sleep()
```

The sequence observed is:

```
Caller starts
Signal starts
Signal finishes
Caller resumes
```

If signals were asynchronous, the caller would continue execution immediately.

Since execution pauses until the signal completes, the signal is synchronous.

---

# Question 2

## Do Django signals run in the same thread?

### Conclusion

Yes.

By default, Django signals execute in the same thread as the caller.

### Logic

The thread ID is printed both:

* Before saving the model.
* Inside the signal handler.

Example:

```
Caller Thread ID:
140534712

Signal Thread ID:
140534712
```

Since both IDs are identical, the signal executes in the same thread.

---

# Question 3

## Do Django signals run in the same database transaction?

### Conclusion

Yes.

By default, Django signals participate in the same transaction.

### Logic

A transaction is created using:

```python
transaction.atomic()
```

Inside the transaction:

* A model object is saved.
* The signal creates an AuditLog entry.
* An exception is intentionally raised.

The transaction rolls back.

After rollback:

```
SampleModel Count = 0

AuditLog Count = 0
```

Although the signal executed, its database changes were rolled back together with the caller's transaction.

This proves that the signal operates within the same database transaction.

---

# Rectangle Class

## Requirement

The Rectangle class should:

* Accept length and width.
* Support iteration.
* Return:

```
{"length": value}

{"width": value}
```

## Implementation

The iterator is implemented using Python generators.

Example:

```python
rect = Rectangle(10, 5)

for item in rect:
    print(item)
```

Output:

```
{'length': 10}

{'width': 5}
```

---

# How to Run

## Step 1

Clone the repository.

```
git clone https://github.com/A-J-10/accuknox-assignment
```

## Step 2

Create a virtual environment.

Windows:

```
python -m venv venv

venv\Scripts\activate
```


## Step 3

Install dependencies.

```
pip install -r requirements.txt
```

## Step 4

Create migrations.

```
python manage.py makemigrations core
```

## Step 5

Apply migrations.

```
python manage.py migrate
```

## Step 6

Run the test command.

```
python manage.py run_tests
```

---

# Expected Output

The console output demonstrates:

* Signal execution.
* Thread IDs.
* Transaction rollback.
* Rectangle iteration.

Example:

```
Caller Thread:
...

Signal Thread:
...

Signal executed

Transaction rolled back

SampleModel Count:
0

AuditLog Count:
0

[{'length': 10}, {'width': 5}]
```

---

# Technologies Used

* Python
* Django
* SQLite
* Django Signals
* Django ORM

---

# Key Findings

## Django Signals

### Synchronous?

Yes.

### Same Thread?

Yes.

### Same Transaction?

Yes.

---

# References

* Django Official Documentation
* Python Official Documentation

Thank you for reviewing this submission.
