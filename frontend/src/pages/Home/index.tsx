import React from 'react';
import { useTranslation } from 'react-i18next';
import { Typography, Container, Box, Button } from '@mui/material';
import { useNavigate } from 'react-router-dom';

const Home: React.FC = () => {
  const { t } = useTranslation();
  const navigate = useNavigate();

  return (
    <Container maxWidth="md">
      <Box
        sx={{
          display: 'flex',
          flexDirection: 'column',
          alignItems: 'center',
          textAlign: 'center',
          py: 8,
        }}
      >
        <Typography variant="h2" component="h1" gutterBottom>
          {t('common.welcome')}
        </Typography>
        <Typography variant="h5" color="text.secondary" paragraph>
          Practice interviews with AI and improve your skills
        </Typography>
        <Box sx={{ mt: 4 }}>
          <Button
            variant="contained"
            color="primary"
            size="large"
            onClick={() => navigate('/interview')}
            sx={{ mr: 2 }}
          >
            {t('interview.start')}
          </Button>
          <Button
            variant="outlined"
            color="primary"
            size="large"
            onClick={() => navigate('/dashboard')}
          >
            {t('common.dashboard')}
          </Button>
        </Box>
      </Box>
    </Container>
  );
};

export default Home; 