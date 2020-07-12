import React, { Component } from "react";
import Counter from "./counter";

export default class Counters extends Component {
	render() {
		return (
			<div>
				<button
					onClick={this.props.onReset}
					className="btn-primary btn-sm m-2"
				>
					Reset
				</button>
				{this.props.counters.map((counter) => (
					<Counter
						key={counter.id}
						counter={counter}
						selected={true}
						onDelete={this.props.onDelete}
						onAdd={this.props.onAdd}
						onSubtract={this.props.onSubtract}
					/>
				))}
			</div>
		);
	}
}
