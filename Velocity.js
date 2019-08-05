//the below function will calculate the velocity with set parameters
function calculateVelocity(velocity, totalTeamMembers, totalDaysOut, totalDaysInSprint, averageInjections, deploys) {
    const deployTime = deploys * 2;
    //console.log(deployTime);
        
    const totalHoursOutPerSprint = totalDaysOut * 6 + deployTime;
    //console.log(totalHoursOutPerSprint);
    
    const totalDaysOutPerSprint = totalHoursOutPerSprint / 6;
    //console.log(totalDaysOutPerSprint);
    
    const velocityPerPersonPerDay = velocity / (totalDaysInSprint * totalTeamMembers);
    //console.log(velocityPerPersonPerDay);
    
    const planFor = velocity - (totalDaysOutPerSprint * velocityPerPersonPerDay) - (averageInjections * 2);
    console.log("Plan For " + Math.round(planFor));
};

calculateVelocity(55, 6, 12, 10, 9, 4);

//add loop for people in sprint to count hours
//add each person to the page to be able to count hours and create a feed from ADP and Outlook to count for you


