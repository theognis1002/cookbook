import React, { Component } from "react";

export default class Counter extends Component {
	render() {
		return (
			<div>
				<span className={this.getBadgeClasses()}>
					{this.formatCount()}
				</span>
				<button
					onClick={() => this.props.onAdd(this.props.counter)}
					className="btn btn-secondary btn-sm m-2"
				>
					+
				</button>
				<button
					onClick={() => this.props.onSubtract(this.props.counter)}
					className="btn btn-secondary btn-sm m-2"
				>
					-
				</button>
				<button
					onClick={() => this.props.onDelete(this.props.counter.id)}
					className="btn btn-danger btn-sm m-2"
				>
					Delete
				</button>
			</div>
		);
	}

	getBadgeClasses() {
		let classes = "badge m-2 badge-";
		if (this.props.counter.value === 0) {
			classes += "warning";
		} else if (this.props.counter.value > 0) {
			classes += "primary";
		} else {
			classes += "danger";
		}
		return classes;
	}

	formatCount() {
		const { value } = this.props.counter;
		return value === 0 ? 0 : value;
	}
}
