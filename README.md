# WinterShelterPortal – Shelter Management Portal for Congregations
WinterShelterPortal (WSP) is a secure, web-based application built with Ignition Perspective, designed for congregations and partner organizations participating in the Homeless Management System initiative.
Each organization uses the portal to register, configure, and manage its own shelter offerings — including beds, availability, schedules, and guest information
It provides a simple, mobile-friendly interface for accessing real-time shelter availability across participating organizations.

## Purpose
The portal is intended for internal use by individual congregations or shelter partners. It provides tools to:

* Register and configure your shelter location(s)

* Manage bed availability and intake schedules

* View detailed participant information (specific to your shelter only)

* Track historical statistics and activity

This project is part of the OpenHMShub platform and depends on shared logic and components from the `Global` project.

## Requirements
`Ignition 8.1.47` or later

Database with Discovery_Schema.sql and Discovery_Master_Data.sql already loaded

[`Global`](https://github.com/OpenHMShub/Global) project must be cloned and configured first

## Project Structure
[Documentation](https://github.com/OpenHMShub/Documentation/wiki/Winter-Shelter-Portal)

[User Roles and Permissions](https://github.com/OpenHMShub/Documentation/wiki/User-Roles-and-Permissions)

[ERD](https://github.com/OpenHMShub/Documentation/wiki/Entity-Relationship-Diagrams) 

## Installation
[Instalation Guide](https://github.com/OpenHMShub/Documentation/wiki/Instalation-Guide)

Clone the repository into your Ignition projects directory:

Linux:
`/usr/local/bin/ignition/data/projects`

Windows:
`C:\Program Files\Inductive Automation\Ignition\data\projects`

```bash
git clone https://github.com/OpenHMShub/WinterShelterPortal.git
```
Restart your Ignition Gateway.

Ensure that the Global project is present and correctly inherited:
In the Gateway, go to `Config` → `System` → `Projects` and verify that Global is listed as a parent project of WinterShelterPortal.

Launch the application in your browser:
`http://localhost:8088/data/perspective/client/WinterShelterPortal/`

## Related Projects
[Global](https://github.com/OpenHMShub/Global)

[HMS](https://github.com/OpenHMShub/HMS)

[MobileHMS](https://github.com/OpenHMShub/MobileHMS)
