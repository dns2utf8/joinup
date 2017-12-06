# Installation

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

If the `venv` command fails, try this one:
```bash
rm -rf venv
virtualenv --python=python3.6 venv
```

# Architecture decisions

* Group names must start with a capital letter for compatibility reason

# Open Tasks

* [ ] Test with PostgreSQL for bigger loads
* [ ] Review search box
* [ ] Archiving
    * [ ] Events
    * [ ] Groups
    * [ ] Tags
* [ ] Deleting archived
    * [ ] Events
    * [ ] Groups
    * [ ] Tags
* [ ] Tags
    * [ ] Propose new Tags on the fly
    * [ ] Better edit/search form
* [ ] Group
    * [ ] Create Event
    * [ ] Join
    * [ ] Leave
* [ ] Event
    * [ ] Join
    * [ ] Leave