# iCalendar translator for Carnegie Library of Pittsburgh events

A simple tool for getting the Carnegie Library of Pittsburgh (CLP) events
calendar in iCalendar (ICS) format (e.g. for importing in Google Calendar).

The CLP events website actually has native support for ICS but it generates
invalid output with extra empty lines at the start, which confuses Google
Calendar. This tool simply strips those lines.

## Deployment

Deploy to any platform that supports Flask (e.g. Google App Engine).

## Usage

Use the /events endpoint to get the events in iCalendar format. Optional
parameters are supported to filter the returned events:

* category: filter by event category

  Value | Category
  ------|---------
  108   | Author Visits
  110   | Book Discussions
  107   | Classes & Workshops
  435   | Family Fun
  112   | Film Screening
  118   | Fundraisers
  116   | Games, Crafts & Activities
  114   | Health & Fitness
  217   | Language Classes
  115   | Parties & Celebrations
  111   | Performances
  113   | Playtime
  109   | Presentations & Lectures
  493   | Social Gatherings
  117   | Special Events
  106   | Storytimes
  3567  | Tours & Group Visits

* location: filter by library location

  Value | Location
  ------|---------
  526   | Allegheny
  622   | Beechview
  647   | Brookline
  667   | Carrick
  673   | Downtown & Business
  727   | East Liberty
  729   | Hazelwood
  731   | Hill District
  732   | Homewood
  733   | Knoxville
  734   | Lawrenceville
  1161  | Library for the Blind and Physically Handicapped
  435   | Main (Oakland)
  735   | Mt. Washington
  736   | Sheraden
  740   | South Side
  741   | Squirrel Hill
  742   | West End
  548   | Woods Run

* age-group: filter by event target age group

  Value | Age Group
  ------|----------
  39    | Adults
  4034  | Early Learners Birth-5 Years
  38    | Kids Birth-Grade 5
  1759  | School Age Kids Grades K-5
  103   | Teens
  102   | Tweens

For example, to get the list of language classes for adults at the main
(Oakland) library, use `/events?category=217&location=435&age-group=39`.
