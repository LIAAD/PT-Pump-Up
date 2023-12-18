import AuthenticatedLayout from '@/Layouts/AuthenticatedLayout';
import { Head } from '@inertiajs/react';
import './../../css/login.css';
import Button from '@mui/material/Button';
import { router } from '@inertiajs/react'

export default function Dashboard({ auth, api_token }) {

    const submitForm = (e) => {
        e.preventDefault();
        router.post('/tokens')
    }


    return (
        <AuthenticatedLayout
            user={auth.user}
            header={<h2 className="font-semibold text-xl text-gray-800 leading-tight">Dashboard</h2>}
        >
            <Head title="Dashboard" />

            <div className="py-12">
                <div className="max-w-7xl mx-auto sm:px-6 lg:px-8">
                    <div className="bg-white overflow-hidden shadow-sm sm:rounded-lg">
                        <div className="p-6 text-gray-900">You're logged in!</div>
                    </div>
                </div>
                <div className="max-w-7xl mx-auto sm:px-6 lg:px-8 mt-5">
                    <div className="bg-white overflow-hidden shadow-sm sm:rounded-lg">
                        {api_token && <div className="p-6 text-gray-900">Bearer Token: {api_token} </div>}
                        {!api_token &&
                            <Button sx={{ width: "100%" }} onClick={submitForm}>
                                <div className="p-6 text-gray-900">
                                    Generate Bearer Token
                                </div>
                            </Button>
                        }
                    </div>
                </div>
            </div>
        </AuthenticatedLayout>
    );
}
