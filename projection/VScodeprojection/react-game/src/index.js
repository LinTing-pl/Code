import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";

function Square(props) {
    return (
        <button className="square" onClick={props.onClick}>
            {props.value}
        </button>
    );
}

function calculateWinner(squares) {
    const lines = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6],
    ];
    for (let i = 0; i < lines.length; i++) {
        const [a, b, c] = lines[i];
        if (squares[a] && squares[a] === squares[b] && squares[a] === squares[c]) {
            return [squares[a], lines[i]];
        }
    }
    return;
}

class Board extends React.Component {
    renderSquare(i) {
        return (
            <Square
                key={i}
                value={this.props.squares[i]}
                onClick={() => {
                    this.props.onClick(i);
                }}
            />
        );
    }

    render() {
        const n = this.props.n;
        let k = 0;
        let board = [];
        for (let i = 0; i < n; i++) {
            let boardRow = [];
            for (let j = 0; j < n; j++) {
                boardRow.push(this.renderSquare(k++));
            }
            board.push(
                <div className="board-row" key={i}>
                    {boardRow}
                </div>
            );
        }
        return <div>{board}</div>;
    }
}

class Game extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            history: [
                {
                    squares: Array(9),
                },
            ],
            stepNumber: 0,
            XIsNext: true,
            ordinate: [],
            n: 3,
            flag: true,
        };
    }

    handleClick(i) {
        const history = this.state.history.slice(0, this.state.stepNumber + 1);
        const curr = history[history.length - 1];
        const squares = [...curr.squares];
        const ordinate = this.state.ordinate.slice(0, this.state.stepNumber);

        if (squares[i] || calculateWinner(squares)) return;
        squares[i] = this.state.XIsNext ? "X" : "O";
        this.setState({
            XIsNext: !this.state.XIsNext,
            history: history.concat([{squares: squares}]),
            stepNumber: history.length,
            ordinate: [...ordinate, [squares[i], Math.floor(i / 3), i % 3]],
        });
        const winner = calculateWinner(squares);
        this.hightLight([0, 1, 2, 3, 4, 5, 6, 7, 8], "black");
        if (winner) {
            this.hightLight(winner[1], "red");
        }
        const lis = document.querySelectorAll(".desc");
        const bnts = document.querySelectorAll(".desc button");
        for (let i = 0; i < lis.length; i++) {
            lis[i].style.fontWeight = "500";
            bnts[i].style.fontWeight = "500";
        }
    }

    jumpTo(step) {
        this.setState({
            stepNumber: step,
            XIsNext: step % 2 === 0,
        });
    }

    rr() {
        this.setState({flag: !this.state.flag});
    }

    hightLight(winner, color) {
        let sqs = document.querySelectorAll(".square");
        for (let i = 0; i < winner.length; i++) {
            sqs[winner[i]].style.color = color;
        }
    }

    render() {
        const history = [...this.state.history];
        const curr = history[this.state.stepNumber];
        const winner = calculateWinner(curr.squares);
        let status = winner
            ? "Winner: " + winner[0]
            : "Next player: " + (this.state.XIsNext ? "X" : "O");
        if (this.state.stepNumber === 9 && !winner) {
            status = "平局";
        }
        let lis = [];
        lis = [...this.state.history].map((step, move) => {
            const desc = move
                ? "Go to move #" +
                move +
                " " +
                this.state.ordinate[move - 1][0] +
                JSON.stringify(this.state.ordinate[move - 1].slice(1))
                : "Go to game start";
            return (
                <li key={move} className="desc">
                    <button
                        onClick={() => {
                            return this.jumpTo(move);
                        }}
                    >
                        {desc}
                    </button>
                </li>
            );
        });
        return (
            <div className="game">
                <div className="game-board">
                    <Board
                        squares={curr.squares}
                        n={this.state.n}
                        onClick={(i) => this.handleClick(i)}
                    />
                </div>
                <div className="game-info">
                    <div>{status}</div>
                    <button onClick={() => this.rr()}>
                        {this.state.flag ? "升序" : "降序"}
                    </button>
                    <ol>{this.state.flag ? lis : [...lis].reverse()}</ol>
                </div>
            </div>
        );
    }
}

// ========================================

const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game/>);
