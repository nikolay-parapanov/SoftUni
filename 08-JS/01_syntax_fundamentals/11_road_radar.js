function solve(speed, area) {
    if (area === 'motorway') {
        limit = 130;
        if (speed > limit) {
            over = speed - limit;
            if (over <= 20) {
                statusRecord = 'speeding';
            } else if (over <= 40) {
                statusRecord = 'excessive speeding';
            } else {
                statusRecord = 'reckless driving'
            }
            console.log(`The speed is ${over} km/h faster than the allowed speed of ${limit} - ${statusRecord}`);
        } else {
            console.log(`Driving ${speed} km/h in a ${limit} zone`);
        }
    } else if (area === 'interstate') {
        limit = 90;
        if (speed > limit) {
            over = speed - limit;
            if (over <= 20) {
                statusRecord = 'speeding';
            } else if (over <= 40) {
                statusRecord = 'excessive speeding';
            } else {
                statusRecord = 'reckless driving'
            }
            console.log(`The speed is ${over} km/h faster than the allowed speed of ${limit} - ${statusRecord}`);
        } else {
            console.log(`Driving ${speed} km/h in a ${limit} zone`);
        }
    } else if (area === 'city') {
        limit = 50;
        if (speed > limit) {
            over = speed - limit;
            if (over <= 20) {
                statusRecord = 'speeding';
            } else if (over <= 40) {
                statusRecord = 'excessive speeding';
            } else {
                statusRecord = 'reckless driving'
            }
            console.log(`The speed is ${over} km/h faster than the allowed speed of ${limit} - ${statusRecord}`);
        } else {
            console.log(`Driving ${speed} km/h in a ${limit} zone`);
        }
    } else if (area === 'residential') {
        limit = 20;
        if (speed > limit) {
            over = speed - limit;
            if (over <= 20) {
                statusRecord = 'speeding';
            } else if (over <= 40) {
                statusRecord = 'excessive speeding';
            } else {
                statusRecord = 'reckless driving'
            }
            console.log(`The speed is ${over} km/h faster than the allowed speed of ${limit} - ${statusRecord}`);
        } else {
            console.log(`Driving ${speed} km/h in a ${limit} zone`);
        }
    }

}

solve(40, 'city');
solve(21, 'residential');
solve(120, 'interstate');
solve(200, 'motorway');