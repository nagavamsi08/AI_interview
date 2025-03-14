import React from 'react';
import { useTranslation } from 'react-i18next';
import {
  Container,
  Box,
  Typography,
  Paper,
  Grid,
  LinearProgress,
} from '@mui/material';

const Analytics: React.FC = () => {
  const { t } = useTranslation();

  // Mock data for analytics
  const skillScores = [
    { skill: 'Technical Knowledge', score: 85 },
    { skill: 'Communication', score: 92 },
    { skill: 'Problem Solving', score: 78 },
    { skill: 'Leadership', score: 88 },
    { skill: 'Team Work', score: 95 },
  ];

  const interviewStats = {
    totalInterviews: 15,
    averageScore: 85,
    bestScore: 95,
    worstScore: 70,
    totalDuration: '10h 30m',
  };

  return (
    <Container maxWidth="lg">
      <Box sx={{ py: 4 }}>
        <Typography variant="h4" gutterBottom>
          {t('common.analytics')}
        </Typography>

        <Grid container spacing={3}>
          {/* Overall Stats */}
          <Grid item xs={12} md={6}>
            <Paper sx={{ p: 3 }}>
              <Typography variant="h6" gutterBottom>
                {t('analytics.overview')}
              </Typography>
              <Box sx={{ mt: 2 }}>
                <Typography variant="body1">
                  Total Interviews: {interviewStats.totalInterviews}
                </Typography>
                <Typography variant="body1">
                  Average Score: {interviewStats.averageScore}%
                </Typography>
                <Typography variant="body1">
                  Best Score: {interviewStats.bestScore}%
                </Typography>
                <Typography variant="body1">
                  Worst Score: {interviewStats.worstScore}%
                </Typography>
                <Typography variant="body1">
                  Total Interview Time: {interviewStats.totalDuration}
                </Typography>
              </Box>
            </Paper>
          </Grid>

          {/* Skill Analysis */}
          <Grid item xs={12} md={6}>
            <Paper sx={{ p: 3 }}>
              <Typography variant="h6" gutterBottom>
                {t('analytics.technicalScore')}
              </Typography>
              <Box sx={{ mt: 2 }}>
                {skillScores.map((skill) => (
                  <Box key={skill.skill} sx={{ mb: 2 }}>
                    <Box sx={{ display: 'flex', justifyContent: 'space-between', mb: 1 }}>
                      <Typography variant="body1">{skill.skill}</Typography>
                      <Typography variant="body1">{skill.score}%</Typography>
                    </Box>
                    <LinearProgress
                      variant="determinate"
                      value={skill.score}
                      sx={{ height: 8, borderRadius: 4 }}
                    />
                  </Box>
                ))}
              </Box>
            </Paper>
          </Grid>

          {/* Progress Over Time */}
          <Grid item xs={12}>
            <Paper sx={{ p: 3 }}>
              <Typography variant="h6" gutterBottom>
                {t('analytics.progress')}
              </Typography>
              <Box sx={{ height: 300, display: 'flex', alignItems: 'center', justifyContent: 'center' }}>
                <Typography color="text.secondary">
                  Chart component will be implemented here
                </Typography>
              </Box>
            </Paper>
          </Grid>

          {/* Areas for Improvement */}
          <Grid item xs={12}>
            <Paper sx={{ p: 3 }}>
              <Typography variant="h6" gutterBottom>
                {t('analytics.improvement')}
              </Typography>
              <Box sx={{ mt: 2 }}>
                <Typography variant="body1" paragraph>
                  1. Work on improving problem-solving skills through more practice interviews
                </Typography>
                <Typography variant="body1" paragraph>
                  2. Focus on technical communication and explaining complex concepts
                </Typography>
                <Typography variant="body1" paragraph>
                  3. Practice behavioral questions and STAR method responses
                </Typography>
              </Box>
            </Paper>
          </Grid>
        </Grid>
      </Box>
    </Container>
  );
};

export default Analytics; 