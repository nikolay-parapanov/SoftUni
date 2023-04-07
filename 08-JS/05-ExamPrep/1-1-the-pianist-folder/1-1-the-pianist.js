function thePianist(input) {
  let numberOfPieces = Number(input.splice(0, 1)[0]);
  let arrPieces = [];
  let piecesObjects = {};

  for (let index = 0; index < numberOfPieces; index++) {
    let currentPiece = input.splice(0, 1);
    let splitResult = currentPiece[0].split("|");
    let [piece, composer, key] = currentPiece[0].split("|");
    piecesObjects[piece] = { composer, key };
  }

  for (let index = 0; index < input.length - 1; index++) {
    let currentRecord = input[index].split("|");
    let currentCommand = currentRecord[0];
    let currentPiece = currentRecord[1];

    if (currentCommand === "Add") {
      if (!piecesObjects.hasOwnProperty(currentPiece)) {
        let currentComposer = currentRecord[2];
        let currentKey = currentRecord[3];
        piecesObjects[currentPiece] = { currentComposer, currentKey };
        console.log(piecesObjects[currentPiece]);
        for (const piece in piecesObjects) {
          let {composer, key } = piecesObjects[piece];
          console.log(`${piece} -> Composer: ${composer}, Key: ${key}`)
          }
        console.log(`${currentPiece} by ${currentComposer} in ${currentKey} added to the collection!`
        );
      } else console.log(`${currentPiece} is already in the collection!`);
    } else if (currentCommand === "Remove") {
      if (piecesObjects.hasOwnProperty(currentPiece)) {
        delete piecesObjects[currentPiece];
        console.log(`Successfully removed ${currentPiece}!`);
      } else
        console.log(
          `Invalid operation! ${currentPiece} does not exist in the collection.`
        );
    } else if (currentCommand === "ChangeKey") {
      if (piecesObjects.hasOwnProperty(currentPiece)) {
        let newKey = currentRecord[2];
        piecesObjects[currentPiece].key = newKey;
        console.log(`Changed the key of ${currentPiece} to ${newKey}!`);
      } else
        console.log(
          `Invalid operation! ${currentPiece} does not exist in the collection.`
        );
    }
  }


  console.log('______________________________');
  for (const piece in piecesObjects) {
    let {composer, key } = piecesObjects[piece];
    console.log(`${piece} -> Composer: ${composer}, Key: ${key}`)
    }
  }

thePianist([
  "3",
  "Fur Elise|Beethoven|A Minor",
  "Moonlight Sonata|Beethoven|C# Minor",
  "Clair de Lune|Debussy|C# Minor",
  "Add|Sonata No.2|Chopin|B Minor",
  "Add|Fur Elise|Beethoven|C# Minor",
  "Stop",
]);
