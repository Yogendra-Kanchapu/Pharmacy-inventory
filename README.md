# InvenRx: Pharmacy Inventory Management System

## Overview
InvenRx is a web-based application designed to facilitate the management of pharmacy inventory. It enables users to add new items to the inventory, review existing stock, and make necessary edits or deletions. This document provides an overview of the system's functionalities and how to interact with it.

## Features
* Home: The landing page that provides a navigation bar to access all functionalities.
* Add New Item: A form to input new stock items into the inventory database.
* Review and Edit Stock: A list of current inventory items with options to edit or delete each entry.

## Getting Started
The application is structured with the following endpoints:
### Home (/)
The homepage serves as the starting point of the application. It contains navigation links to all primary functions.

### Add New Item (/enternew)
This page presents a form for entering the details of a new stock item, such as product name, category, quantity, and price.

### Review and Edit Stock (/list)
Displays a complete list of inventory items. Each item has an associated 'Edit' option that directs users to a form pre-populated with the item's details for easy modification.

## Technical Documentation
### Database Structure
The application connects to a SQLite database named pharmacy_inventory.db. The primary table used for inventory management is Stock, which includes columns for Product, Category, Quantity, and Price.

### Backend Routes
* Add Record (/addrec): Handles POST requests to insert new items into the Stock table.
* Edit Record (/edit): Selects an item for editing based on its row ID and presents an editable form.
* Update Record (/editrec): Processes POST requests to update existing inventory items.
* Delete Record (/delete): Deletes an item from the Stock table based on its row ID.

### Error Handling
The application includes basic error handling for database operations, and implementing commit/rollback transactions to maintain data integrity. Error messages are displayed to the user if any operation fails.

### Security Measures
SQL injection prevention is implemented by using parameterized queries with placeholders (?).

### Deployment
The application is hosted on Render, a cloud service that enables users to build and run web applications. Debug mode is enabled for development purposes.

### Usage Notes
In production, it is recommended to disable the debug mode to secure the application against potential security threats. Ensure that you have proper backups of the database before performing large-scale operations.

