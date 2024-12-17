/*
   New Perspectives on JavaScript, 2nd Edition
  
   Author: Anjum Shams
   Date:   7/23/20

   Function List:
   dayDiff(start, stop)
      Calculates the number of days, rounded down the next lowest integer, 
      between a starting date and stopping date.

   hoursDiff(start, top)
      Calculates the number of hours left in the current day rounded down 
      to the next lowest integer between a starting date and the stopping date.

   minutesDiff(start, stop)
      Calculates the number of minutes left in the current hour rounded down 
      to the next lowest integer between a starting date and the stopping date.

   showDate(time)
      Displays the value of the time object in the format:
      mm/dd/yyyy

   showTime(time)
      Displays the value of the time object in the format:
      hh:mm am/pm
*/

//Create function daysDiff
function daysDiff(start, stop) {
   return Math.floor((stop - start)/(1000*60*60*24));
}

//Create function hoursDiff
function hoursDiff(start, stop) {
   var remainingDays = (stop-start)/(1000*60*60*24);
   return Math.floor((remainingDays - daysDiff(start, stop))*24);
}

//Create function minutesDiff
function minutesDiff(start, stop) {   
   var remainingDays = (stop-start)/(1000*60*60*24);
   var remainingHours = (remainingDays - daysDiff(start, stop))*24;
   return Math.floor((remainingHours - hoursDiff(start, stop))*60);
}

//Create function showDate
function showDate(dateObj) {
   currentDate = dateObj.getDate();
   currentMonth = dateObj.getMonth()+1;
   currentYear = dateObj.getFullYear();
   return currentMonth + "/" + currentDate + "/" + currentYear;
}

//Create function showTime
function showTime(dateObj) {
   currentSecond=dateObj.getSeconds();
   currentMinute=dateObj.getMinutes();
   currentHour=dateObj.getHours();

   //Determine the time display
   var isAmOrPm = (currentHour < 12) ? " a.m." : " p.m.";
   currentHour = (currentHour > 12) ? currentHour - 12 : currentHour;  
   currentHour = (currentHour == 0) ? 12 : currentHour;   
   currentMinute = currentMinute < 10 ? "0"+currentMinute : currentMinute;
   currentSecond = currentSecond < 10 ? "0"+currentSecond : currentSecond;
   return currentHour + ":" + currentMinute + ":" + currentSecond + isAmOrPm;
}
