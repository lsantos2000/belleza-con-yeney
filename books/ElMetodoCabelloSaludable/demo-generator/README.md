# English demo PDF generator

This generator reproduces the 30-page English demo using the same sequence as the approved Spanish demo: seven promotional separators and 23 selected book pages.

From the repository root:

```powershell
python -m venv books/ElMetodoCabelloSaludable/demo-generator/.venv
books/ElMetodoCabelloSaludable/demo-generator/.venv/Scripts/python -m pip install -r books/ElMetodoCabelloSaludable/demo-generator/requirements.txt
books/ElMetodoCabelloSaludable/demo-generator/.venv/Scripts/python books/ElMetodoCabelloSaludable/demo-generator/generate.py
```

The selected source images are stored in `resources/images/books/ElMetodoCabelloSaludable/en/demo-pages/`. The generated public file is `public/The-Healthy-Hair-Method-demo.pdf`.

