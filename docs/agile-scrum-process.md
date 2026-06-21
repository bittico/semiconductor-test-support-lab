# Agile Scrum-Inspired Process

## Overview

This project is organized using Scrum-inspired practices to simulate how an Application Support Engineer may work in a real engineering environment.

Although this is an individual learning project, it follows Agile Scrum concepts such as backlog management, sprint planning, sprint goals, definition of done, validation, and retrospective notes.

The goal is to build the lab incrementally through small, manageable phases, each one delivering a working technical improvement.

## Scrum-Inspired Approach

The project is divided into sprints. Each sprint has a clear technical goal, deliverables, validation steps, and documentation.

| Sprint   | Goal                                                                    | Status    |
| -------- | ----------------------------------------------------------------------- | --------- |
| Sprint 1 | Set up Ubuntu Server, SSH, Git, GitHub, and Python test simulation      | Completed |
| Sprint 2 | Install Jenkins and create a CI/CD pipeline to run the Python simulator | Completed |
| Sprint 3 | Add PostgreSQL to store test results and query metrics                  | Planned   |
| Sprint 4 | Add Nginx dashboard to display test results and application metrics     | Planned   |
| Sprint 5 | Add monitoring and troubleshooting documentation                        | Planned   |
| Sprint 6 | Add STDF-related semiconductor test data concepts                       | Planned   |

## Product Backlog

The product backlog contains the main technical tasks required to complete the lab.

Backlog items include:

* Configure Ubuntu Server networking.
* Enable SSH access from Windows.
* Create GitHub repository.
* Build Python semiconductor test simulator.
* Generate CSV test reports.
* Install Jenkins.
* Create Jenkins pipeline.
* Archive generated reports as build artifacts.
* Add PostgreSQL integration.
* Store test results in a database.
* Build an Nginx-based dashboard.
* Document troubleshooting incidents.
* Add semiconductor STDF-related concepts.

## User Stories

The project uses user stories to describe technical work from the perspective of an engineer or internal customer.

### User Story 1

As an Application Support Engineer,
I want to access the Linux server remotely using SSH,
so that I can manage and troubleshoot application services from a Windows workstation.

### User Story 2

As an engineering user,
I want to run a semiconductor test simulation,
so that I can generate test results for ASIC and FPGA devices.

### User Story 3

As an Application Support Engineer,
I want Jenkins to execute the test simulation automatically,
so that the process is repeatable and does not depend on manual execution.

### User Story 4

As an Application Support Engineer,
I want generated reports to be archived in Jenkins,
so that each pipeline execution keeps evidence of its output.

### User Story 5

As an engineering team member,
I want test results to be stored in PostgreSQL,
so that I can analyze pass rates, failed tests, and execution times.

## Definition of Done

A task is considered done when:

* The technical implementation works successfully.
* The command or configuration has been validated.
* The change is committed to Git.
* The change is pushed to GitHub.
* The README or technical documentation is updated if needed.
* Any relevant issue or troubleshooting step is documented.

## Retrospective Notes

Lessons learned so far:

* Linux networking should be validated from both the Ubuntu VM and the Windows host.
* SSH troubleshooting should include service status, firewall status, IP address, routing, and host connectivity.
* VMware NAT issues can affect Windows-to-Linux connectivity even when the Linux VM is working correctly.
* Jenkins pipelines should produce visible logs and archived artifacts.
* Documentation is important because it shows not only what was built, but also how issues were investigated and resolved.

## Application Support Relevance

This Scrum-inspired approach demonstrates skills relevant to an Application Support Engineering role:

* Working in structured phases.
* Managing a technical backlog.
* Supporting tools used by engineering teams.
* Troubleshooting Linux, Windows, networking, and CI/CD issues.
* Documenting incidents and resolutions.
* Delivering incremental improvements.
* Preparing for collaboration with hardware and software development teams.
