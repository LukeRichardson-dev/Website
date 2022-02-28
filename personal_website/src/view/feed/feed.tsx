import React from "react";
import ReactList from "react-list";
import { FeedItem, FeedItemProps } from "./feed_item";
import './feed.css';


// class FeedItem {
//     constructor(public title: string, public content: string, public views: number) {}
// }

interface FeedState {
    items: Array<FeedItemProps>,
}

export interface FeedProps {}

export class Feed extends React.Component<FeedProps, FeedState> {

    state: FeedState = {
        items: [
            {
                title: "Test Title",
                content: "React typescript test",
                views: 204
            }
        ],
    };

    constructor(props: FeedProps) {
        super(props);

        this.renderItem = this.renderItem.bind(this);
    }
    
    renderItem(index: number, key: number | string): JSX.Element {
        const {items} = this.state;

        return <div key={key}>

            <FeedItem {...items[index]} />

        </div>
    }

    render(): React.ReactNode {

        return <div style={{overflow: 'auto', maxHeight: 400}}>
            <ReactList 
                itemRenderer={this.renderItem}
                length={this.state.items.length}
                type='uniform'
            /> 
        </div>;
    }
}

