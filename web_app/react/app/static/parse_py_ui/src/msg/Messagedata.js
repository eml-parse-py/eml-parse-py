import React from 'react';


const MsgData = (props) => {

    return (
        <div id={"msg-headers"}>
            {(props.msg_data || []).map(item => (

                <ul key={item}>
                    <ul> {item[0]}: {item[1]}</ul>
                </ul>)
            )}
            <br/>

        </div>

    );

}


export default MsgData;