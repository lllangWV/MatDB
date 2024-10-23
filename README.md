# MatDB

MatDB is a material science database designed to be light weight and portable. It is built on top of Apache Parquet files using PyArrow, which reduces the overhead of serialization and allows for efficient storage and retrieval of complex data types.

## Table of Contents

- [Features](#features)
- [Why MatDB?](#why-matdb)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Usage](#usage)
  - [Creating a Database](#creating-a-database)
  - [Adding Data](#adding-data)
  - [Reading Data](#reading-data)
  - [Updating Data](#updating-data)
  - [Deleting Data](#deleting-data)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Simple Interface**: Easy-to-use methods for creating, reading, updating, and deleting data.
- **High Performance**: Utilizes Apache Parquet and PyArrow for efficient data storage and retrieval.
- **Supports Complex Data Types**: Handles nested and complex data types without serialization overhead.
- **Scalable**: Designed to handle large datasets efficiently.
- **Schema Evolution**: Supports adding new fields and updating schemas seamlessly.

## Installation

Install MatDB using pip:

```bash
pip install matdb
```

## Quick Start

```python
from matdb import MatDB

# Initialize the database
db = MatDB('path/to/db')

# Create data
properties={
    'density': 7.8,
    'volume': 22.1
}
structure=Structure.from_spacegroup("Fm-3m", Lattice.cubic(4.1437), ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]])
data={'structure': structure, 'properties': properties}


# Add data to the database
db.add(structure=structure, properties=properties, table_name='materials')

# Read data from the database
materials_table = db.read(table_name='materials')
print(materials_table.to_pandas())
```

## Usage

### Creating a Database

Initialize a MatDB instance by specifying the path to the database directory:

```python
from matdb import MatDB

db = MatDB('path/to/db')
```

### Adding Data

Add data to the database using the `create` method. Data can be a dictionary, a list of dictionaries, or a Pandas DataFrame.

```python

properties={
    'density': 7.8,
    'volume': 22.1
}
data_list = [
    {'structure': Structure.from_spacegroup("Fm-3m", Lattice.cubic(4.1437), ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]]), 'properties': properties},
    {'structure': Structure.from_spacegroup("Fm-3m", Lattice.cubic(4.1437), ["Cs", "Cl"], [[0, 0, 0], [0.5, 0.5, 0.5]]), 'properties': properties}
]

db.add_many(dadata_listta, table_name='materials')
```

### Reading Data

Read data from the database using the `read` method. You can filter data by IDs, specify columns, and apply filters.

```python
# Read all data
all_materials = db.read(table_name='materials')

# Read specific columns
names = db.read(table_name='materials', columns=['name'])

# Read data with filters
from pyarrow import compute as pc

age_filter = pc.field('age') > 30
older_materials = db.read(table_name='materials', filters=[age_filter])
```

### Updating Data

Update existing records in the database using the `update` method. Each record must include the `id` field.

```python
update_data = [
    {'id': 0, 'property_1': 'metal'},
    {'id': 2, 'property_2': 'gas'}
]

db.update(update_data, table_name='materials')
```

### Deleting Data

Delete records from the database by specifying their IDs.

```python
db.delete(ids=[0, 3], table_name='materials')
```


## Contributing

Contributions are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

*Note: This project is in its initial stages. Features and APIs are subject to change. Please refer to the latest documentation and release notes for updates.*