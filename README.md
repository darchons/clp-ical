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

* eventcategory: filter by event category

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

* venues: filter by library location

  Value | Location
  ------|---------
  1281  | Allegheny
  1283  | Beechview
  1284  | Brookline
  1285  | Carrick
  1286  | Downtown
  46    | East Liberty
  1287  | Hazelwood
  1289  | Hill District
  1288  | Homewood
  1290  | Knoxville
  1291  | Lawrenceville
  1292  | LAMP
  1280  | Main (Oakland)
  1293  | Mt. Washington
  1294  | Sheraden
  1295  | South Side
  1296  | Squirrel Hill
  1297  | West End
  1298  | Woods Run

For example, to get the list of language classes at the main
(Oakland) library, use `/events?eventcategory=217&venues=1280
