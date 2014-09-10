Currently still in development

Flask server connecting with dc.js on the front end.


TODO (DATA-WISE):

1. Put data into SQL file instead of pandas
2. Use Flask streaming method to stream data to index (this will make streaming be server side instead of d3 generating XHR requests)

TODO (GRAPHICS-WISE):

1. Make total timeline with count per day (#day-total)
2. Bar chart with avg daily use per hour filtered by selection in #1 (#hourly-avg)
3. Trip duration histogram (filtered by selection in #1 /#2)
4. Subscriber/Customer pie chart (one time user or subscriber), filtered by #1 and subsequent
5. Male/female pie chart (data only available for Subscribers, filtered by #1 and subsequent )
6. Data table for start stop, listing by most frequent (filtered by #1 and subsequent)
7. Data table for end stop, listing by most frequent (filtered by #2 and subsequent)

Potentially replace #6 and #7 with map for most frequent routes, but only as final step after previous stuff working.
