# WinterShelterPortal – Shelter Management Portal for Congregations
WinterShelterPortal (WSP) is a secure, web-based application built with Ignition Perspective, designed for congregations and partner organizations participating in the Room In The Inn initiative.
Each organization uses the portal to register, configure, and manage its own shelter offerings — including beds, availability, schedules, and guest information
It provides a simple, mobile-friendly interface for accessing real-time shelter availability across participating organizations.

## Purpose
The portal is intended for internal use by individual congregations or shelter partners. It provides tools to:

* Register and configure your shelter location(s)

* Manage bed availability and intake schedules

* View detailed participant information (specific to your shelter only)

* Track historical statistics and activity

This project is part of the OpenHMSHub platform and depends on shared logic and components from the `Global` project.

## Requirements
`Ignition 8.1.45` or later

Database with Discovery_Schema.sql and Discovery_Master_Data.sql already loaded

[`Global`](https://github.com/OpenHMSHub/Global) project must be cloned and configured first

## Project Structure
[Documentation](https://github.com/OpenHMSHub/Documentation/wiki/Winter-Shelter-Portal)

[User Roles and Permissions](https://github.com/OpenHMSHub/Documentation/wiki/User-Roles-and-Permissions)

[ERD](https://github.com/OpenHMSHub/Documentation/wiki/Entity-Relationship-Diagrams) 

## Installation
[Instalation Guide](https://github.com/OpenHMSHub/Documentation/wiki/Instalation-Guide)

Clone the repository into your Ignition projects directory:

Linux:
`/usr/local/bin/ignition/data/projects`

Windows:
`C:\Program Files\Inductive Automation\Ignition\data\projects`

```bash
git clone https://github.com/OpenHMSHub/WinterShelterPortal.git
```
Restart your Ignition Gateway.

Ensure that the Global project is present and correctly inherited:
In the Gateway, go to `Config` → `System` → `Projects` and verify that Global is listed as a parent project of WinterShelterPortal.

Launch the application in your browser:
`http://localhost:8088/data/perspective/client/WinterShelterPortal/`

## Related Projects
[Global](https://github.com/OpenHMSHub/Global)

[RITI](https://github.com/OpenHMSHub/RITI)

[Discovery](https://github.com/OpenHMSHub/Discovery)
