import ShowResource from '@/Components/ShowResource';
import PTPumpUpLayout from '@/Layouts/PTPumpUpLayout';
import React from 'react'

const Show = (props) => {
    return (
        <PTPumpUpLayout
            main={
                <ShowResource elem={props.dataset} delete_route="datasets.destroy" auth={props.auth} />
            }
        />
    )
}

export default Show