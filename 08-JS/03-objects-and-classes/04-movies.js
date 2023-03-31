function movieParser(input) {
    let movies = [];

    for (const line of input) {
        let commandTokens = line.split(' ');

        if (line.includes('addMovie')) {
            let movieName = commandTokens.slice(1).join(' ');
            addMovie(movieName);
        } else if (line.includes('directedBy')) {
            let indexOfCommand = commandTokens.indexOf('directedBy');
            let movieName = commandTokens.slice(0, indexOfCommand).join(' ');
            let director = commandTokens.slice(indexOfCommand + 1).join(' ');
            addDirector(movieName, director);
        } else {
            let indexOfCommand = commandTokens.indexOf('onDate');
            let movieName = commandTokens.slice(0, indexOfCommand).join(' ');
            let date = commandTokens.slice(indexOfCommand + 1).join(' ')
            addDate(movieName, date)
        }
    }

    let filteredMovies = movies
        .filter((movie) => movie.hasOwnProperty('name') && movie.hasOwnProperty('director') && movie.hasOwnProperty('date'))
    for (const movie of filteredMovies) {
        console.log(JSON.stringify(movie));
    }

    function addMovie(name) {
        movies.push({ name });
    }

    function addDirector(name, director) {
        let movie = movies.find((m) => m.name === name);
        if (movie) {
            movie.director = director;
        }
    }

    function addDate(name, date) {
        let movie = movies.find((m) => m.name === name)
        if (movie) {
            movie.date = date
        }
    }
}

movieParser(
    [
        'addMovie Fast and Furious',
        'addMovie Godfather',
        'Inception directedBy Christopher Nolan',
        'Godfather directedBy Francis Ford Coppola',
        'Godfather onDate 29.07.2018',
        'Fast and Furious onDate 30.07.2018',
        'Batman onDate 01.08.2018',
        'Fast and Furious directedBy Rob Cohen'
    ]
)