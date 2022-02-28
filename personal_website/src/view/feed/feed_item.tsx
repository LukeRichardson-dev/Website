import React from "react";

export interface FeedItemProps {
    title: string, content: string, views: number
}

export class FeedItem extends React.Component<FeedItemProps> {

    render(): React.ReactNode {
        return <div>
            <h2>{this.props.title}</h2>
            <p>{this.props.content}</p>

        </div>;
    }
}
