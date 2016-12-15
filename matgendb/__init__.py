"""
Pymatgen-db is a database add-on for the Python Materials Genomics (pymatgen)
materials analysis library. It enables the creation of Materials
Project-style MongoDB databases for management of materials data and
provides a clean and intuitive web ui for exploring that data. A query engine
is also provided to enable the easy translation of MongoDB docs to useful
pymatgen objects for analysis purposes.
"""

__author__ = "Shyue Ping Ong, Dan Gunter"
__date__ = "Dec 3 2016"
__version__ = "0.6.5"


from .query_engine import QueryEngine
