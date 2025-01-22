const sqlite3 = require('sqlite3').verbose();
const db = new sqlite3.Database(':memory:'); // In-memory database for simplicity

// Create tokens table
db.serialize(() => {
  db.run("CREATE TABLE tokens (type TEXT, value TEXT)");
});

const lexer = (input) => {
  const tokens = [];
  const tokenTypes = [
    { regex: /\d+/, type: 'NUMBER' },
    { regex: /[+\-*/]/, type: 'OPERATOR' },
    { regex: /\s+/, type: 'WHITESPACE' }
  ];

  let index = 0;
  while (index < input.length) {
    let match = null;
    let type = null;

    for (const tokenType of tokenTypes) {
      match = input.substring(index).match(tokenType.regex);
      if (match && match.index === 0) {
        type = tokenType.type;
        break;
      }
    }

    if (type && type !== 'WHITESPACE') {
      tokens.push({ type, value: match[0] });
    }

    index += match[0].length;
  }

  return tokens;
};

// Sample input
const input = "12 + 34 * 56";

const tokens = lexer(input);

// Store tokens in the database
db.serialize(() => {
  const insertStmt = db.prepare("INSERT INTO tokens (type, value) VALUES (?, ?)");
  tokens.forEach(token => {
    insertStmt.run(token.type, token.value);
  });
  insertStmt.finalize();
});

// Retrieve and log tokens from the database
db.serialize(() => {
  db.each("SELECT type, value FROM tokens", (err, row) => {
    console.log(`Token: ${row.type}, Value: ${row.value}`);
  });
});

// Close the database connection
db.close();
