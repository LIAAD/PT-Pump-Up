import React from 'react'

const Publication = (props) => {
    const getString = (publication) =>
        publication.format("bibliography", {
            template: "apa",
            "html": true,
        })

    return (
        <li>{getString(props.publication)}</li>
    )
}

export default Publication