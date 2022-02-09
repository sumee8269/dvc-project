    from setuptools import setup,find_packages

    with open("README.md","r", encoding="utf-8") as f:
        long_description = f.read()

    setup(
        name="src",
        version="0.0.1",
        author="sumee8269",
        description = "A small package for dcv ml pipeline demo",
        long_description= long_description,
        url = "https://github.com/sumee8269/simple-dvc-project.git",
        long_description_content_type = "text/markdown",
        author_email="sumit.thakur12492@gmail.com",
        package_dir={"":"src"},
        packages=find_packages(where="src"),
        license="GNU",
        python_requires = ">=3.6",
        install_requires = ['dvc','dvc[gdrive]','dvc[s3]','pandas',
                            'scikit_learn']

    )
