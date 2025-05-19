import React, { useState } from 'react';
import {
    Card,
    CardContent,
    CardHeader,
} from '@mui/material/Card';
import {
    FormControl,
    InputLabel,
    Select,
    MenuItem,
    TextField,
} from '@mui/material';
import { styled } from '@mui/material/styles';
import { Box } from '@mui/system';

const DebateLMWebsite = () => {
    const [leftDropdownValue, setLeftDropdownValue] = useState('');
    const [rightDropdownValue, setRightDropdownValue] = useState('');
    const [leftInputValue, setLeftInputValue] = useState('');
    const [rightInputValue, setRightInputValue] = useState('');

    const Logo = styled('h1')({
        position: 'absolute',
        top: '1rem',
        left: '50%',
        transform: 'translateX(-50%)',
        textAlign: 'center',
        fontSize: '2.5rem',
        fontWeight: 'bold',
        background: 'linear-gradient(to right, #3b82f6, #8b5cf6)', // Tailwind's blue-400 to purple-400
        WebkitBackgroundClip: 'text',
        WebkitTextFillColor: 'transparent',
    });

    return (
        <Box
            sx={{
                minHeight: '100vh',
                backgroundImage:
                    'linear-gradient(to bottom, #1f2937, #4c1d95, #000000)', // Tailwind's from-gray-900, via-purple-900, to-black
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                padding: '1rem',
            }}
        >
            <Logo>DebateLM</Logo>
            <Card
                sx={{
                    width: '100%',
                    maxWidth: '800px', // Increased max-width for larger screens
                    backgroundColor: 'rgba(255, 255, 255, 0.05)', // Equivalent to bg-white/5
                    backdropFilter: 'blur(10px)', // backdrop-blur-md
                    borderRadius: '0.75rem', // rounded-xl
                    boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)', // shadow-2xl approximation
                    border: '1px solid rgba(255, 255, 255, 0.1)', // border-white/10
                    transition: 'transform 0.5s, box-shadow 0.5s', // Smooth transition
                    '&:hover': {
                        transform: 'scale(1.01)', // hover:scale-[1.01]
                        boxShadow:
                            '0 20px 25px -5px rgba(107, 114, 128, 0.2), 0 8px 10px -6px rgba(107, 114, 128, 0.1)', // Approximation of hover:shadow-purple-500/20 - increased spread
                    },
                }}
            >
                <CardHeader
                    title={
                        <h2
                            style={{
                                fontSize: '1.5rem', // text-xl
                                fontWeight: '600', // font-semibold
                                color: 'white', // text-white
                                margin: 0,
                            }}
                        >
                            Enter your query
                        </h2>
                    }
                    sx={{
                        textAlign: 'center',
                        paddingTop: '3rem', // pt-12
                        paddingBottom: '2rem', // pb-8
                    }}
                />
                <CardContent
                    sx={{
                        paddingBottom: '2rem', // pb-8 (consistent padding)
                    }}
                >
                    <Box
                        sx={{
                            display: 'flex',
                            flexDirection: { xs: 'column', sm: 'row' },
                            alignItems: 'center',
                            justifyContent: 'center',
                            gap: '1.5rem', // gap-6
                        }}
                    >
                        <Box
                            sx={{
                                width: { xs: '100%', sm: '50%' },
                                display: 'flex',
                                flexDirection: 'column',
                                gap: '1rem', // space-y-4
                            }}
                        >
                            <FormControl
                                fullWidth
                                variant="outlined"
                                sx={{
                                    '& .MuiOutlinedInput-root': {
                                        backgroundColor:
                                            'rgba(0, 0, 0, 0.2)', // bg-black/20
                                        color: 'white', // text-white
                                        borderColor:
                                            'rgba(167, 139, 250, 0.3)', // border-purple-500/30
                                        '&:hover .MuiOutlinedInput-notchedOutline': {
                                            borderColor:
                                                'rgba(167, 139, 250, 0.5)', // hover:border-purple-500/50
                                        },
                                        '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
                                            borderColor:
                                                'rgba(167, 139, 250, 0.5)', // focus:border-purple-500/50
                                            boxShadow:
                                                '0 0 0 0.2rem rgba(167, 139, 250, 0.25)', // focus:ring-purple-500/50 approximation
                                        },
                                    },
                                    '& .MuiInputLabel-outlined': {
                                        color: 'white', // text-white
                                    },
                                    '& .MuiSelect-icon': {
                                        color: 'white', // text-white
                                    },
                                    '& .MuiList-root': {
                                        backgroundColor: '#374151', // bg-gray-800
                                        color: 'white',
                                    },
                                }}
                            >
                                <InputLabel id="left-dropdown-label">
                                    Select an option
                                </InputLabel>
                                <Select
                                    labelId="left-dropdown-label"
                                    value={leftDropdownValue}
                                    onChange={(e) =>
                                        setLeftDropdownValue(e.target.value)
                                    }
                                    label="Select an option"
                                >
                                    <MenuItem value="option1">Option 1</MenuItem>
                                    <MenuItem value="option2">Option 2</MenuItem>
                                    <MenuItem value="option3">Option 3</MenuItem>
                                </Select>
                            </FormControl>
                            <TextField
                                fullWidth
                                variant="outlined"
                                placeholder="Enter input"
                                value={leftInputValue}
                                onChange={(e) =>
                                    setLeftInputValue(e.target.value)
                                }
                                sx={{
                                    '& .MuiOutlinedInput-root': {
                                        backgroundColor:
                                            'rgba(0, 0, 0, 0.2)', // bg-black/20
                                        color: 'white', // text-white
                                        borderColor:
                                            'rgba(167, 139, 250, 0.3)', // border-purple-500/30
                                        '&:hover .MuiOutlinedInput-notchedOutline': {
                                            borderColor:
                                                'rgba(167, 139, 250, 0.5)', // hover:border-purple-500/50
                                        },
                                        '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
                                            borderColor:
                                                'rgba(167, 139, 250, 0.5)', // focus:border-purple-500/50
                                            boxShadow:
                                                '0 0 0 0.2rem rgba(167, 139, 250, 0.25)', // focus:ring-purple-500/50 approximation
                                        },
                                    },
                                    '& .MuiInputLabel-outlined': {
                                        color: 'rgba(156, 163, 175, 1)', // placeholder:text-gray-400
                                    },
                                }}
                                InputLabelProps={{
                                    style: {
                                        color: leftInputValue
                                            ? 'white'
                                            : 'rgba(156, 163, 175, 1)', // Keep label color consistent
                                    },
                                }}
                            />
                        </Box>
                        <Box
                            sx={{
                                width: { xs: '100%', sm: '50%' },
                                display: 'flex',
                                flexDirection: 'column',
                                gap: '1rem', // space-y-4
                            }}
                        >
                            <FormControl
                                fullWidth
                                variant="outlined"
                                sx={{
                                    '& .MuiOutlinedInput-root': {
                                        backgroundColor:
                                            'rgba(0, 0, 0, 0.2)', // bg-black/20
                                        color: 'white', // text-white
                                        borderColor:
                                            'rgba(167, 139, 250, 0.3)', // border-purple-500/30
                                        '&:hover .MuiOutlinedInput-notchedOutline': {
                                            borderColor:
                                                'rgba(167, 139, 250, 0.5)', // hover:border-purple-500/50
                                        },
                                        '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
                                            borderColor:
                                                'rgba(167, 139, 250, 0.5)', // focus:border-purple-500/50
                                            boxShadow:
                                                '0 0 0 0.2rem rgba(167, 139, 250, 0.25)', // focus:ring-purple-500/50 approximation
                                        },
                                    },
                                    '& .MuiInputLabel-outlined': {
                                        color: 'white', // text-white
                                    },
                                    '& .MuiSelect-icon': {
                                        color: 'white', // text-white
                                    },
                                    '& .MuiList-root': {
                                        backgroundColor: '#374151', // bg-gray-800
                                        color: 'white',
                                    },
                                }}
                            >
                                <InputLabel id="right-dropdown-label">
                                    Select an option
                                </InputLabel>
                                <Select
                                    labelId="right-dropdown-label"
                                    value={rightDropdownValue}
                                    onChange={(e) =>
                                        setRightDropdownValue(e.target.value)
                                    }
                                    label="Select an option"
                                >
                                    <MenuItem value="optionA">Option A</MenuItem>
                                    <MenuItem value="optionB">Option B</MenuItem>
                                    <MenuItem value="optionC">Option C</MenuItem>
                                </Select>
                            </FormControl>
                            <TextField
                                fullWidth
                                variant="outlined"
                                placeholder="Enter input"
                                value={rightInputValue}
                                onChange={(e) =>
                                    setRightInputValue(e.target.value)
                                }
                                sx={{
                                    '& .MuiOutlinedInput-root': {
                                        backgroundColor:
                                            'rgba(0, 0, 0, 0.2)', // bg-black/20
                                        color: 'white', // text-white
                                        borderColor:
                                            'rgba(167, 139, 250, 0.3)', // border-purple-500/30
                                        '&:hover .MuiOutlinedInput-notchedOutline': {
                                            borderColor:
                                                'rgba(167, 139, 250, 0.5)', // hover:border-purple-500/50
                                        },
                                        '&.Mui-focused .MuiOutlinedInput-notchedOutline': {
                                            borderColor:
                                                'rgba(167, 139, 250, 0.5)', // focus:border-purple-500/50
                                            boxShadow:
                                                '0 0 0 0.2rem rgba(167, 139, 250, 0.25)', // focus:ring-purple-500/50 approximation
                                        },
                                    },
                                    '& .MuiInputLabel-outlined': {
                                        color: 'rgba(156, 163, 175, 1)', // placeholder:text-gray-400
                                    },
                                }}
                                InputLabelProps={{
                                    style: {
                                        color: rightInputValue
                                            ? 'white'
                                            : 'rgba(156, 163, 175, 1)', // Keep label color consistent
                                    },
                                }}
                            />
                        </Box>
                    </Box>
                    <Box
                        sx={{
                            textAlign: 'center',
                            marginTop: '2rem', // mt-8
                        }}
                    >
                        <button
                            style={{
                                padding: '0.75rem 2rem', // px-8 py-3
                                borderRadius: '1rem', // rounded-full
                                background:
                                    'linear-gradient(to right, #8b5cf6, #3b82f6)', // from-purple-500 to-blue-500
                                color: 'white', // text-white
                                boxShadow:
                                    '0px 10px 10px rgba(107, 114, 128, 0.5)', // shadow-lg approximation
                                transition:
                                    'transform 0.3s, box-shadow 0.3s, background-image 0.3s', // Smooth transition
                                border: 'none',
                                cursor: 'pointer',
                                fontSize: '1rem',
                                fontWeight: '500',
                            }}
                            onMouseEnter={(e) => {
                                e.currentTarget.style.transform = 'scale(1.05)'; // hover:scale-105
                                e.currentTarget.style.boxShadow =
                                    '0px 12px 12px rgba(107, 114, 128, 0.3)'; // hover:shadow-purple-500/50 approximation - reduced opacity
                                e.currentTarget.style.backgroundImage =
                                    'linear-gradient(to right, #9333ea, #2563eb)'; // hover:from-purple-600 hover:to-blue-600
                            }}
                            onMouseLeave={(e) => {
                                e.currentTarget.style.transform = 'scale(1)';
                                e.currentTarget.style.boxShadow =
                                    '0px 10px 10px rgba(107, 114, 128, 0.5)'; // original shadow
                                e.currentTarget.style.backgroundImage =
                                    'linear-gradient(to right, #8b5cf6, #3b82f6)'; // original gradient
                            }}
                        >
                            Submit
                        </button>
                    </Box>
                </CardContent>
            </Card>
        </Box>
    );
};

export default DebateLMWebsite;
