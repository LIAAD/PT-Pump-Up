import React from 'react'
import Divider from '@mui/material/Divider';
import Chip from '@mui/material/Chip';

const InescDivider = (props) => {
    return (
        <Divider className="divider" sx={{ my: 5 }}>
            <Chip label={props.label} sx={{ p: 5 }} />
        </Divider>
    )
}

export default InescDivider